import os
from dotenv import load_dotenv

load_dotenv(".env")
load_dotenv(os.getenv("ENV_FILE"))

from app.config import Config, Network
from app.ergo.appkit import ErgoAppKit, ErgoValueT


CFG = Config[Network]
DEBUG = True # CFG.DEBUG

class TestNFTLockedVesting:

    appKit = ErgoAppKit(CFG.node, Network, CFG.explorer)

    with open(f'app/contracts/NFTLockedVesting.es') as f:
        unformattedScript = f.read()
        script = unformattedScript.format(**{})
    contract = appKit.compileErgoScript(script)

    vestedTokenId = '81ba2a45d4539045995ad6ceeecf9f14b942f944a1c9771430a89c3f88ee898a'
    vestingKey = 'f9e5ce5aa0d95f5d54a7bc89c46730d9662397067250aa18a0039631c0f5b809'

    duration = int(1000*60*60*24)

    vestingInputBox = appKit.buildInputBox(int(1e6), 
            {
                vestedTokenId: 999999
            }, 
            [
            #Vesting key
            appKit.ergoValue(vestingKey, ErgoValueT.ByteArrayFromHex),  
            #Redeem period
            appKit.ergoValue(duration,ErgoValueT.Long),    
            #Redeem amount per period              
            appKit.ergoValue(int(999999/365),ErgoValueT.Long),     
            #Start vesting april 1st                      
            appKit.ergoValue(int(1648771200000),ErgoValueT.Long),    
            #Total vested                   
            appKit.ergoValue(int(999999),ErgoValueT.Long)                               
            ], 
            contract)

    def test_normal_redeem(self):          
        userInputBox = self.appKit.buildInputBox(int(2e6), 
            {
                self.vestingKey: 1
            }, 
            registers=None, contract=self.appKit.dummyContract())

        #Set the preheader to 2.5 days after vesting start, so 2*redeem amount should be free to claim
        preHeader = self.appKit.preHeader(timestamp=int(1648771200000+self.duration*2.5))

        newVestingBox = self.appKit.buildOutBox(self.vestingInputBox.getValue(), {
                self.vestedTokenId: int(999999-int(999999/365)*2)
            },
            [
            #Vesting key
            self.appKit.ergoValue(self.vestingKey, ErgoValueT.ByteArrayFromHex),  
            #Redeem period
            self.appKit.ergoValue(self.duration,ErgoValueT.Long),    
            #Redeem amount per period              
            self.appKit.ergoValue(int(999999/365),ErgoValueT.Long),     
            #Start vesting april 1st                      
            self.appKit.ergoValue(int(1648771200000),ErgoValueT.Long),    
            #Total vested                   
            self.appKit.ergoValue(int(999999),ErgoValueT.Long)                               
            ], self.contract)

        newUserBox = self.appKit.buildOutBox(int(1e6), {
            self.vestingKey: 1,
            self.vestedTokenId: int(999999/365)*2
            }, registers=None, contract=self.appKit.dummyContract())

        unsignedTx = self.appKit.buildUnsignedTransaction(
            inputs = [self.vestingInputBox, userInputBox],
            outputs = [newVestingBox,newUserBox],
            fee = int(1e6),
            sendChangeTo = self.appKit.dummyContract().getAddress().getErgoAddress(),
            preHeader = preHeader
        )
        signed = False
        try:
            signedTx = self.appKit.signTransaction(unsignedTx)
            signed = True
        except Exception as e:
            signed = False
    
        assert signed