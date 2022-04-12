import java.io
import java.lang
import java.util
import java.util.concurrent
import typing



class AbstractOwnableSynchronizer(java.io.Serializable): ...

class Condition:
    def awaitNanos(self, long: int) -> int: ...
    def awaitUninterruptibly(self) -> None: ...
    def awaitUntil(self, date: java.util.Date) -> bool: ...
    def signal(self) -> None: ...
    def signalAll(self) -> None: ...

class Lock:
    def lock(self) -> None: ...
    def lockInterruptibly(self) -> None: ...
    def newCondition(self) -> Condition: ...
    @typing.overload
    def tryLock(self) -> bool: ...
    @typing.overload
    def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    def unlock(self) -> None: ...

class LockSupport:
    @staticmethod
    def getBlocker(thread: java.lang.Thread) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def park() -> None: ...
    @typing.overload
    @staticmethod
    def park(object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def parkNanos(object: typing.Any, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def parkNanos(long: int) -> None: ...
    @typing.overload
    @staticmethod
    def parkUntil(object: typing.Any, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def parkUntil(long: int) -> None: ...
    @staticmethod
    def unpark(thread: java.lang.Thread) -> None: ...

class ReadWriteLock:
    def readLock(self) -> Lock: ...
    def writeLock(self) -> Lock: ...

class StampedLock(java.io.Serializable):
    def __init__(self): ...
    def asReadLock(self) -> Lock: ...
    def asReadWriteLock(self) -> ReadWriteLock: ...
    def asWriteLock(self) -> Lock: ...
    def getReadLockCount(self) -> int: ...
    @staticmethod
    def isLockStamp(long: int) -> bool: ...
    @staticmethod
    def isOptimisticReadStamp(long: int) -> bool: ...
    @staticmethod
    def isReadLockStamp(long: int) -> bool: ...
    def isReadLocked(self) -> bool: ...
    @staticmethod
    def isWriteLockStamp(long: int) -> bool: ...
    def isWriteLocked(self) -> bool: ...
    def readLock(self) -> int: ...
    def readLockInterruptibly(self) -> int: ...
    def toString(self) -> str: ...
    def tryConvertToOptimisticRead(self, long: int) -> int: ...
    def tryConvertToReadLock(self, long: int) -> int: ...
    def tryConvertToWriteLock(self, long: int) -> int: ...
    def tryOptimisticRead(self) -> int: ...
    @typing.overload
    def tryReadLock(self) -> int: ...
    @typing.overload
    def tryReadLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    def tryUnlockRead(self) -> bool: ...
    def tryUnlockWrite(self) -> bool: ...
    @typing.overload
    def tryWriteLock(self) -> int: ...
    @typing.overload
    def tryWriteLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    def unlock(self, long: int) -> None: ...
    def unlockRead(self, long: int) -> None: ...
    def unlockWrite(self, long: int) -> None: ...
    def validate(self, long: int) -> bool: ...
    def writeLock(self) -> int: ...
    def writeLockInterruptibly(self) -> int: ...

class AbstractQueuedLongSynchronizer(AbstractOwnableSynchronizer, java.io.Serializable):
    def acquire(self, long: int) -> None: ...
    def acquireInterruptibly(self, long: int) -> None: ...
    def acquireShared(self, long: int) -> None: ...
    def acquireSharedInterruptibly(self, long: int) -> None: ...
    def getExclusiveQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getFirstQueuedThread(self) -> java.lang.Thread: ...
    def getQueueLength(self) -> int: ...
    def getQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getSharedQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getWaitQueueLength(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> int: ...
    def getWaitingThreads(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> java.util.Collection[java.lang.Thread]: ...
    def hasContended(self) -> bool: ...
    def hasQueuedPredecessors(self) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> bool: ...
    def isQueued(self, thread: java.lang.Thread) -> bool: ...
    def owns(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> bool: ...
    def release(self, long: int) -> bool: ...
    def releaseShared(self, long: int) -> bool: ...
    def toString(self) -> str: ...
    def tryAcquireNanos(self, long: int, long2: int) -> bool: ...
    def tryAcquireSharedNanos(self, long: int, long2: int) -> bool: ...
    class ConditionObject(Condition, java.io.Serializable):
        def __init__(self, abstractQueuedLongSynchronizer: 'AbstractQueuedLongSynchronizer'): ...
        def awaitNanos(self, long: int) -> int: ...
        def awaitUninterruptibly(self) -> None: ...
        def awaitUntil(self, date: java.util.Date) -> bool: ...
        def signal(self) -> None: ...
        def signalAll(self) -> None: ...

class AbstractQueuedSynchronizer(AbstractOwnableSynchronizer, java.io.Serializable):
    def acquire(self, int: int) -> None: ...
    def acquireInterruptibly(self, int: int) -> None: ...
    def acquireShared(self, int: int) -> None: ...
    def acquireSharedInterruptibly(self, int: int) -> None: ...
    def getExclusiveQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getFirstQueuedThread(self) -> java.lang.Thread: ...
    def getQueueLength(self) -> int: ...
    def getQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getSharedQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getWaitQueueLength(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> int: ...
    def getWaitingThreads(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> java.util.Collection[java.lang.Thread]: ...
    def hasContended(self) -> bool: ...
    def hasQueuedPredecessors(self) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> bool: ...
    def isQueued(self, thread: java.lang.Thread) -> bool: ...
    def owns(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> bool: ...
    def release(self, int: int) -> bool: ...
    def releaseShared(self, int: int) -> bool: ...
    def toString(self) -> str: ...
    def tryAcquireNanos(self, int: int, long: int) -> bool: ...
    def tryAcquireSharedNanos(self, int: int, long: int) -> bool: ...
    class ConditionObject(Condition, java.io.Serializable):
        def __init__(self, abstractQueuedSynchronizer: 'AbstractQueuedSynchronizer'): ...
        def awaitNanos(self, long: int) -> int: ...
        def awaitUninterruptibly(self) -> None: ...
        def awaitUntil(self, date: java.util.Date) -> bool: ...
        def signal(self) -> None: ...
        def signalAll(self) -> None: ...

class ReentrantLock(Lock, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    def getHoldCount(self) -> int: ...
    def getQueueLength(self) -> int: ...
    def getWaitQueueLength(self, condition: Condition) -> int: ...
    def hasQueuedThread(self, thread: java.lang.Thread) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, condition: Condition) -> bool: ...
    def isFair(self) -> bool: ...
    def isHeldByCurrentThread(self) -> bool: ...
    def isLocked(self) -> bool: ...
    def lock(self) -> None: ...
    def lockInterruptibly(self) -> None: ...
    def newCondition(self) -> Condition: ...
    def toString(self) -> str: ...
    @typing.overload
    def tryLock(self) -> bool: ...
    @typing.overload
    def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    def unlock(self) -> None: ...

class ReentrantReadWriteLock(ReadWriteLock, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    def getQueueLength(self) -> int: ...
    def getReadHoldCount(self) -> int: ...
    def getReadLockCount(self) -> int: ...
    def getWaitQueueLength(self, condition: Condition) -> int: ...
    def getWriteHoldCount(self) -> int: ...
    def hasQueuedThread(self, thread: java.lang.Thread) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, condition: Condition) -> bool: ...
    def isFair(self) -> bool: ...
    def isWriteLocked(self) -> bool: ...
    def isWriteLockedByCurrentThread(self) -> bool: ...
    def readLock(self) -> 'ReentrantReadWriteLock.ReadLock': ...
    def toString(self) -> str: ...
    def writeLock(self) -> 'ReentrantReadWriteLock.WriteLock': ...
    class ReadLock(Lock, java.io.Serializable):
        def lock(self) -> None: ...
        def lockInterruptibly(self) -> None: ...
        def newCondition(self) -> Condition: ...
        def toString(self) -> str: ...
        @typing.overload
        def tryLock(self) -> bool: ...
        @typing.overload
        def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
        def unlock(self) -> None: ...
    class WriteLock(Lock, java.io.Serializable):
        def getHoldCount(self) -> int: ...
        def isHeldByCurrentThread(self) -> bool: ...
        def lock(self) -> None: ...
        def lockInterruptibly(self) -> None: ...
        def newCondition(self) -> Condition: ...
        def toString(self) -> str: ...
        @typing.overload
        def tryLock(self) -> bool: ...
        @typing.overload
        def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
        def unlock(self) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.util.concurrent.locks")``.

    AbstractOwnableSynchronizer: typing.Type[AbstractOwnableSynchronizer]
    AbstractQueuedLongSynchronizer: typing.Type[AbstractQueuedLongSynchronizer]
    AbstractQueuedSynchronizer: typing.Type[AbstractQueuedSynchronizer]
    Condition: typing.Type[Condition]
    Lock: typing.Type[Lock]
    LockSupport: typing.Type[LockSupport]
    ReadWriteLock: typing.Type[ReadWriteLock]
    ReentrantLock: typing.Type[ReentrantLock]
    ReentrantReadWriteLock: typing.Type[ReentrantReadWriteLock]
    StampedLock: typing.Type[StampedLock]