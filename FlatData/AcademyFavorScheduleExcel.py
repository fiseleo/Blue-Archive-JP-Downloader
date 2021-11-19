# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AcademyFavorScheduleExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AcademyFavorScheduleExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAcademyFavorScheduleExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AcademyFavorScheduleExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AcademyFavorScheduleExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def ScheduleGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def OrderInGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def Location(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AcademyFavorScheduleExcel
    def LocalizeScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def FavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def SecretStoneAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def ScenarioSriptGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyFavorScheduleExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # AcademyFavorScheduleExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # AcademyFavorScheduleExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AcademyFavorScheduleExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # AcademyFavorScheduleExcel
    def RewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # AcademyFavorScheduleExcel
    def RewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # AcademyFavorScheduleExcel
    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AcademyFavorScheduleExcel
    def RewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # AcademyFavorScheduleExcel
    def RewardAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # AcademyFavorScheduleExcel
    def RewardAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # AcademyFavorScheduleExcel
    def RewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AcademyFavorScheduleExcel
    def RewardAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

def Start(builder): builder.StartObject(12)
def AcademyFavorScheduleExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def AcademyFavorScheduleExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(1, CharacterId, 0)
def AcademyFavorScheduleExcelAddCharacterId(builder, CharacterId):
    """This method is deprecated. Please switch to AddCharacterId."""
    return AddCharacterId(builder, CharacterId)
def AddScheduleGroupId(builder, ScheduleGroupId): builder.PrependInt64Slot(2, ScheduleGroupId, 0)
def AcademyFavorScheduleExcelAddScheduleGroupId(builder, ScheduleGroupId):
    """This method is deprecated. Please switch to AddScheduleGroupId."""
    return AddScheduleGroupId(builder, ScheduleGroupId)
def AddOrderInGroup(builder, OrderInGroup): builder.PrependInt64Slot(3, OrderInGroup, 0)
def AcademyFavorScheduleExcelAddOrderInGroup(builder, OrderInGroup):
    """This method is deprecated. Please switch to AddOrderInGroup."""
    return AddOrderInGroup(builder, OrderInGroup)
def AddLocation(builder, Location): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(Location), 0)
def AcademyFavorScheduleExcelAddLocation(builder, Location):
    """This method is deprecated. Please switch to AddLocation."""
    return AddLocation(builder, Location)
def AddLocalizeScenarioId(builder, LocalizeScenarioId): builder.PrependUint32Slot(5, LocalizeScenarioId, 0)
def AcademyFavorScheduleExcelAddLocalizeScenarioId(builder, LocalizeScenarioId):
    """This method is deprecated. Please switch to AddLocalizeScenarioId."""
    return AddLocalizeScenarioId(builder, LocalizeScenarioId)
def AddFavorRank(builder, FavorRank): builder.PrependInt64Slot(6, FavorRank, 0)
def AcademyFavorScheduleExcelAddFavorRank(builder, FavorRank):
    """This method is deprecated. Please switch to AddFavorRank."""
    return AddFavorRank(builder, FavorRank)
def AddSecretStoneAmount(builder, SecretStoneAmount): builder.PrependInt64Slot(7, SecretStoneAmount, 0)
def AcademyFavorScheduleExcelAddSecretStoneAmount(builder, SecretStoneAmount):
    """This method is deprecated. Please switch to AddSecretStoneAmount."""
    return AddSecretStoneAmount(builder, SecretStoneAmount)
def AddScenarioSriptGroupId(builder, ScenarioSriptGroupId): builder.PrependInt64Slot(8, ScenarioSriptGroupId, 0)
def AcademyFavorScheduleExcelAddScenarioSriptGroupId(builder, ScenarioSriptGroupId):
    """This method is deprecated. Please switch to AddScenarioSriptGroupId."""
    return AddScenarioSriptGroupId(builder, ScenarioSriptGroupId)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def AcademyFavorScheduleExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def StartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AcademyFavorScheduleExcelStartRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelTypeVector(builder, numElems)
def AddRewardParcelId(builder, RewardParcelId): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelId), 0)
def AcademyFavorScheduleExcelAddRewardParcelId(builder, RewardParcelId):
    """This method is deprecated. Please switch to AddRewardParcelId."""
    return AddRewardParcelId(builder, RewardParcelId)
def StartRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def AcademyFavorScheduleExcelStartRewardParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelIdVector(builder, numElems)
def AddRewardAmount(builder, RewardAmount): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(RewardAmount), 0)
def AcademyFavorScheduleExcelAddRewardAmount(builder, RewardAmount):
    """This method is deprecated. Please switch to AddRewardAmount."""
    return AddRewardAmount(builder, RewardAmount)
def StartRewardAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def AcademyFavorScheduleExcelStartRewardAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def AcademyFavorScheduleExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)