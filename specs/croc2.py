"""
Croc 2 opcodes
"""

from stratigise.common import SectionInfo

def readOpcode(strat):
	return strat.readInt32LE()

def processSections(strat):
	# TODO: This is temporary
	strat.file.seek(0, 2)
	l = strat.getPos()
	
	return [
		SectionInfo('code', 0, l, ".DIS", params = {}),
	]

opcodes = {
	0x00: ['CommandError'],
	0x01: ['Local', 'int32'],
	0x02: ['Global', 'int32'],
	0x03: ['WorldGlobal', 'int32'],
	0x04: ['AlienVar', 'int32'],
	0x05: ['LocalAddress', 'int32'],
	0x06: ['GlobalAddress', 'int32'],
	0x07: ['WorldGlobalAddress', 'int32'],
	0x08: ['AlienVarAddress', 'int32'],
	0x09: ['Print', 'int32'],
	0x0A: ['Number', 'int32'],
	0x0B: ['UMinus'],
	0x0C: ['Increase'],
	0x0D: ['Decrease'],
	0x0E: ['Add'],
	0x0F: ['Sub'],
	0x10: ['Mul'],
	0x11: ['Div'],
	0x12: ['Equals'],
	0x13: ['Compare'],
	0x14: ['LessThan'],
	0x15: ['GreaterThan'],
	0x16: ['SetModel'],
	0x17: ['Scale'],
	0x18: ['ScaleX'],
	0x19: ['ScaleY'],
	0x1A: ['Scalez'],
	0x1B: ['Shadow', 'int32'],
	0x1C: ['ShadowSize'],
	0x1D: ['ShadowType'],
	0x1E: ['Hide', 'int32'],
	0x1F: ['Flash'], # nop
	0x20: ['Trans'], # nop
	0x21: ['MoveUp'],
	0x22: ['MoveDown'],
	0x23: ['MoveForward'],
	0x24: ['MoveBackward'],
	0x25: ['MoveLeft'],
	0x26: ['MoveRight'],
	0x27: ['TurnRight'],
	0x28: ['TurnLeft'],
	0x29: ['TiltLeft'],
	0x2A: ['TiltRight'],
	0x2B: ['TiltForward'],
	0x2C: ['TiltBackward'],
	0x2D: ['TurnToPlayerX'],
	0x2E: ['TurnToPlayerY'],
	0x2F: ['TurnToPlayerXY'],
	0x30: ['TurnToX'],
	0x31: ['TurnToY'],
	0x32: ['TurnToXY'],
	0x33: ['Wobble'],
	0x34: ['ReSetPos'],
	0x35: ['SetPos'],
	0x36: ['Jump', 'offset32'],
	0x37: ['ObjectFall'],
	0x38: ['Hang', 'int32'],
	0x39: ['WPFirst'],
	0x3A: ['WPLast'],
	0x3B: ['WPNext'],
	0x3C: ['WPPrev'],
	0x3D: ['WPDel'], # nop
	0x3E: ['WPNew'], # nop
	0x3F: ['WPNearest'],
	0x40: ['WPFurthest'],
	0x41: ['WPTurnToX'],
	0x42: ['WPTurnToY'],
	0x43: ['WPTurnToXY'],
	0x44: ['AnimPlay'],
	0x45: ['AnimStop'],
	0x46: ['AnimClear'],
	0x47: ['AnimSetSpeed'], # nop
	0x48: ['CollisionType'],
	0x49: ['CollRadius'],
	0x4A: ['CollHeight'], # nop
	0x4B: ['Collextent'],
	0x4C: ['CollView'], # nop
	0x4D: ['CollPoints'],
	0x4E: ['CollSetPoint'],
	0x4F: ['CreateTrigger', 'int32', 'int32'],
	0x50: ['KillTrigger', 'int32'],
	0x51: ['HoldTriggers'],
	0x52: ['ReleaseTriggers'],
	0x53: ['HoldTrigger', 'int32'],
	0x54: ['ReleaseTrigger', 'int32'],
	0x55: ['Wait'],
	0x56: ['Hold'],
	0x57: ['Release'], # nop
	0x58: ['Remove'],
	0x59: ['MapRemove'],
	0x5A: ['MapAdd'], # nop
	0x5B: ['MapReplace'], # nop
	0x5C: ['Activated'],
	0x5D: ['Collected'],
	0x5E: ['Spawn'],
	0x5F: ['SpawnFrom', 'int32'],
	0x60: ['Link'], # nop
	0x61: ['Unlink'], # nop
	0x62: ['SoundShift'],
	0x63: ['SoundStop'],
	0x64: ['CdPlay'],
	0x65: ['MidiLoop'], # nop
	0x66: ['MidiVolume'], # nop
	0x67: ['CdFade'],
	0x68: ['MidiStop'], # nop
	0x69: ['MidiQueue'], # nop
	0x6A: ['IsLight'], # psx nop
	0x6B: ['LightCol'], # psx nop
	0x6C: ['LightFade'], # psx nop
	0x6D: ['LightAtten'], # psx nop
	0x6E: ['LightType'], # psx nop
	0x6F: ['CollisionOn', 'int32'],
	0x70: ['CollisionOff', 'int32'],
	0x71: ['CollisionOffAll'],
	0x72: ['SoundPlay'],
	0x73: ['SoundPlay'],
	0x74: ['SoundPlayAss'],
	0x75: ['SoundPlayAss'],
	0x76: ['Int'],
	0x77: ['Sin'],
	0x78: ['Cos'],
	0x79: ['Not'],
	0x7A: ['Pop'],
	0x7B: ['StkCmp', 'int32'],
	0x7C: ['Address', 'int32'],
	0x7D: ['Jsr', 'offset32'],
	0x7E: ['JsrImm', 'offset32'],
	0x7F: ['Return'],
	0x80: ['Beq', 'offset32'],
	0x81: ['Bne', 'offset32'],
	0x82: ['BeqImm', 'offset32'],
	0x83: ['BneImm', 'offset32'],
	0x84: ['JumpImm', 'offset32'],
	0x85: ['EndStrat'],
	0x86: ['IsPlayer'],
	0x87: ['And'],
	0x88: ['Or'],
	# This is the point where I have stopped documenting new functions in order.
	# Index_Jump looks fun :P
	0x89: ['Index_Jump'],
	0x8A: ['BitwiseAnd'],
	0x8B: ['Ext_Local'],
	0x8C: ['Ext_LocalAddress'],
	0x8D: ['Ext_Global'],
	0x8E: ['Ext_GlobalAddress'],
	0x8F: ['ObjectJump'],
	0x90: ['Ext_AlienVar'],
	0x91: ['Ext_AlienVarAddress'],
	0x92: ['NotEqual'],
	0x93: ['ShiftLeft'],
	0x94: ['ShiftRight'],
	0x95: ['AnimAdvance'],
	0x96: ['GreaterEqual'],
	0x97: ['LessEqual'],
	0x98: ['Rnd'],
	0x99: ['Blink'],
	0x9A: ['LoseHeart'],
	0x9B: ['ResettoCheckPoint'],
	0x9C: ['ForceCollision'],
	0x9D: ['TurnFromPlayerY'],
	0x9E: ['PlayerAttack'],
	0x9F: ['Rumble'],
	0xA0: ['Vibrate'],
	0xA1: ['SuspendIfTooFar'],
	0xA2: ['CollisionBone'],
	0xA3: ['UseBone'],
	0xA4: ['IsCamera'],
	0xA5: ['Lookatme'],
	0xA6: ['Lookatme'],
	0xA7: ['PushCamera'],
	0xA8: ['PopCamera'],
	0xA9: ['ResetCamerapos'],
	0xAA: ['GainHeart'],
	0xAB: ['GainHeartPot'],
	0xAC: ['AddInv'],
	0xAD: ['GainCrystal'],
	0xAE: ['Cutscene'],
	0xAF: ['Inventory'],
	0xB0: ['Debugname'],
	0xB1: ['PlayerdistanceCheck'],
	0xB2: ['SoundPlay'],
	0xB3: ['SoundPlayass'],
	0xB4: ['SoundAddress'],
	0xB5: ['Onground'],
	0xB6: ['ObjectFallslow'],
	0xB7: ['Player_AlienVar'],
	0xB8: ['Player_AlienVarAddress'],
	0xB9: ['CollisionOffset'],
	0xBA: ['Abs'],
	0xBB: ['Pickup'],
	0xBC: ['Min'],
	0xBD: ['Max'],
	0xBE: ['Spawnparticle'],
	0xBF: ['Sgn'],
	0xC0: ['Spawnafter'],
	0xC1: ['Camera_AlienVar'],
	0xC2: ['Camera_AlienVarAddress'],
	0xC3: ['Target_AlienVar'],
	0xC4: ['Target_AlienVarAddress'],
	0xC5: ['Collide_AlienVar'], # nop
	0xC6: ['Collide_AlienVarAddress'], # nop
	0xC7: ['Target_AlienVar'],
	0xC8: ['Target_AlienVarAddress'],
	0xC9: ['DontLookatme'],
	0xCA: ['Runat'],
	0xCB: ['MoveForwardq'],
	0xCC: ['MoveBackwardq'],
	0xCD: ['Screenprint'],
	0xCE: ['SoundPlay'],
	0xCF: ['SoundPlayass'],
	0xD0: ['SetWP'],
	0xD1: ['ResetWP'],
	0xD2: ['SoundVolume'],
	0xD3: ['Push'],
	0xD4: ['String'],
	0xD5: ['SetbossHearts'],
	0xD6: ['LosebossHeart'],
	0xD7: ['SoundShiftrelative'],
	0xD8: ['Smin'],
	0xD9: ['Isboss'],
	0xDA: ['Topsay'],
	0xDB: ['Boss_AlienVar'],
	0xDC: ['Boss_AlienVarAddress'],
	0xDD: ['Getparentpos'],
	0xDE: ['Afterboss'],
	0xDF: ['AfterPlayer'],
	0xE0: ['BeforePlayer'],
	0xE1: ['Beforeboss'],
	0xE2: ['Nohang', 'int32'],
	0xE3: ['Zero'],
	0xE4: ['Tophead'],
	0xE5: ['Topdialog'],
	0xE6: ['Bottomsay'],
	0xE7: ['Bottomhead'],
	0xE8: ['Bottomdialog'],
	0xE9: ['GetPlayerpos'],
	0xEA: ['GetWPpos'],
	0xEB: ['Getbosspos'],
	0xEC: ['Getdoorpos'],
	0xED: ['Fadeout'],
	0xEE: ['Fadein'],
	0xEF: ['MoveUpq'],
	0xF0: ['MoveDownq'],
	0xF1: ['ForcePlayerdist'],
	0xF2: ['ShadeType'],
	0xF3: ['Nop'],
	0xF4: ['SetanimSpeed'],
	0xF5: ['Checkleveldoor'],
	0xF6: ['BottomheadLeft'],
	0xF7: ['TopheadLeft'],
	0xF8: ['Gainjigsaw'],
	0xF9: ['Gaingoldengobbo'],
	0xFA: ['GainCrystal'],
	0xFB: ['Resetspline'],
	0xFC: ['CheckPoint'],
	0xFD: ['Watertest'],
	0xFE: ['IsmainCamera'],
	0xFF: ['Resetdialog'],
	0x100: ['Endlevel'],
	0x101: ['Dialog_AlienVar'],
	0x102: ['Dialog_AlienVarAddress'],
	0x103: ['Isdialog'],
	0x104: ['Distance'],
	0x105: ['Binocs'],
	0x106: ['Topclosedialog'],
	0x107: ['Bottomclosedialog'],
	0x108: ['Nextinventory'],
	0x109: ['Previnventory'],
	0x10A: ['Otherpiece'],
	0x10B: ['Normalpiece'],
	0x10C: ['Climb'],
	0x10D: ['Delinv'],
	0x10E: ['Gainreward'],
	0x10F: ['Worldvector'],
	0x110: ['ObjectFallveryslow'],
	0x111: ['Slopecontroller'],
	0x112: ['Levelcomplete'],
	0x113: ['Setlevelflag'],
	0x114: ['Getlevelflag'],
	0x115: ['Calccartilt'],
	0x116: ['MoveLeftq'],
	0x117: ['MoveRightq'],
	0x118: ['Bitwisenot'],
	0x119: ['Borderson'],
	0x11A: ['Bordersoff'],
	0x11B: ['Soundadsr'],
	0x11C: ['Soundadsrrelative'],
	0x11D: ['Rotatepiece'],
	0x11E: ['Set_ambient'],
	0x11F: ['Reset_ambient'],
	0x120: ['Invactive'],
	0x121: ['Invinactive'],
	0x122: ['Samplestatus'],
	0x123: ['ResettoCheckPointnlh'],
	0x124: ['Resetdoor'],
	0x125: ['Storedoor'],
	0x126: ['Camera_modified'],
	0x127: ['PushPlayer'],
	0x128: ['PopPlayer'],
	0x129: ['ReSetPostrn'],
	0x12A: ['Gainitem'],
	0x12B: ['Setitem'],
	0x12C: ['Settimer'],
	0x12D: ['Timeroff'],
	0x12E: ['Distancenoy'],
	0x12F: ['Swim'],
	0x130: ['LoseCrystal'],
	0x131: ['Losereward'],
	0x132: ['Losegoldengobbo'],
	0x133: ['Nexttribe'],
	0x134: ['Prevtribe'],
	0x135: ['Settimerclock'],
	0x136: ['Settimerbomb'],
	0x137: ['Initburpinggame'],
	0x138: ['Closeburpinggame'],
	0x139: ['Credit'],
	0x13A: ['Closecredits'],
	0x13B: ['Showrewardcard'],
	0x13C: ['ShowHearts'],
	0x13D: ['Cwg'],
}

# Not needed for Croc 2 ?
def unevaluate(strat):
	print("Warning: Unevaluate called on Croc 2 strat!")
