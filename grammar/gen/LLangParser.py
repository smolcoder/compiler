# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .LLangListener import LLangListener
    from .LLangVisitor import LLangVisitor
else:
    from LLangListener import LLangListener
    from LLangVisitor import LLangVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"<\u0220\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3")
        buf.write(u"\2\3\2\7\2\u0095\n\2\f\2\16\2\u0098\13\2\3\3\3\3\3\3")
        buf.write(u"\3\3\3\4\3\4\7\4\u00a0\n\4\f\4\16\4\u00a3\13\4\3\4\3")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u00ae\n\6\3\6\3\6")
        buf.write(u"\3\6\3\6\3\7\3\7\5\7\u00b6\n\7\3\b\3\b\7\b\u00ba\n\b")
        buf.write(u"\f\b\16\b\u00bd\13\b\3\b\3\b\3\t\3\t\3\t\7\t\u00c4\n")
        buf.write(u"\t\f\t\16\t\u00c7\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3")
        buf.write(u"\13\3\13\3\f\3\f\3\f\3\f\5\f\u00d6\n\f\3\r\3\r\3\r\3")
        buf.write(u"\r\5\r\u00dc\n\r\3\r\3\r\3\16\3\16\3\16\7\16\u00e3\n")
        buf.write(u"\16\f\16\16\16\u00e6\13\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write(u"\17\3\20\3\20\5\20\u00f0\n\20\3\20\3\20\3\21\3\21\3\21")
        buf.write(u"\7\21\u00f7\n\21\f\21\16\21\u00fa\13\21\3\22\3\22\3\22")
        buf.write(u"\3\23\3\23\3\23\5\23\u0102\n\23\3\24\3\24\3\24\5\24\u0107")
        buf.write(u"\n\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3")
        buf.write(u"\31\3\32\3\32\3\32\3\32\3\33\3\33\5\33\u0119\n\33\3\34")
        buf.write(u"\3\34\3\34\7\34\u011e\n\34\f\34\16\34\u0121\13\34\3\35")
        buf.write(u"\3\35\7\35\u0125\n\35\f\35\16\35\u0128\13\35\3\35\3\35")
        buf.write(u"\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3\37\3\37\3\37\5\37\u013b\n\37\3 \3 \3 \3!\3")
        buf.write(u"!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\5%\u014c\n%\3&\3&")
        buf.write(u"\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3(\3(\5(\u0160\n(\3)\3)\3*\3*\5*\u0166\n*\3+\3+\3+\3")
        buf.write(u"+\3+\3+\7+\u016e\n+\f+\16+\u0171\13+\3+\5+\u0174\n+\3")
        buf.write(u",\3,\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0190\n")
        buf.write(u"\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write(u"\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3")
        buf.write(u"\66\3\66\3\66\7\66\u01a9\n\66\f\66\16\66\u01ac\13\66")
        buf.write(u"\5\66\u01ae\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u01c0")
        buf.write(u"\n\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\7\67\u01d6\n\67\f\67\16\67\u01d9\13\67\38\38\38\39\3")
        buf.write(u"9\39\39\3:\3:\3:\5:\u01e5\n:\3;\3;\3;\3;\3;\3;\3;\3;")
        buf.write(u"\3;\3;\3;\7;\u01f2\n;\f;\16;\u01f5\13;\3<\3<\3<\3<\3")
        buf.write(u"<\3<\3<\5<\u01fe\n<\7<\u0200\n<\f<\16<\u0203\13<\3=\3")
        buf.write(u"=\3=\5=\u0208\n=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C")
        buf.write(u"\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\2\5ltvI\2\4\6\b\n\f")
        buf.write(u"\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>")
        buf.write(u"@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write(u"\u0088\u008a\u008c\u008e\2\t\3\2\24\25\3\2\26\30\4\2")
        buf.write(u"\24\24\31\31\3\2\32\35\3\2\36\37\3\2 !\4\2\n\n\"&\u0217")
        buf.write(u"\2\u0096\3\2\2\2\4\u0099\3\2\2\2\6\u009d\3\2\2\2\b\u00a6")
        buf.write(u"\3\2\2\2\n\u00aa\3\2\2\2\f\u00b5\3\2\2\2\16\u00b7\3\2")
        buf.write(u"\2\2\20\u00c5\3\2\2\2\22\u00ca\3\2\2\2\24\u00ce\3\2\2")
        buf.write(u"\2\26\u00d1\3\2\2\2\30\u00d7\3\2\2\2\32\u00e4\3\2\2\2")
        buf.write(u"\34\u00e9\3\2\2\2\36\u00ed\3\2\2\2 \u00f3\3\2\2\2\"\u00fb")
        buf.write(u"\3\2\2\2$\u0101\3\2\2\2&\u0106\3\2\2\2(\u0108\3\2\2\2")
        buf.write(u"*\u010a\3\2\2\2,\u010c\3\2\2\2.\u010e\3\2\2\2\60\u0110")
        buf.write(u"\3\2\2\2\62\u0112\3\2\2\2\64\u0118\3\2\2\2\66\u011a\3")
        buf.write(u"\2\2\28\u0122\3\2\2\2:\u012b\3\2\2\2<\u013a\3\2\2\2>")
        buf.write(u"\u013c\3\2\2\2@\u013f\3\2\2\2B\u0141\3\2\2\2D\u0144\3")
        buf.write(u"\2\2\2F\u0146\3\2\2\2H\u0149\3\2\2\2J\u014d\3\2\2\2L")
        buf.write(u"\u0153\3\2\2\2N\u015f\3\2\2\2P\u0161\3\2\2\2R\u0165\3")
        buf.write(u"\2\2\2T\u0167\3\2\2\2V\u0175\3\2\2\2X\u017b\3\2\2\2Z")
        buf.write(u"\u017e\3\2\2\2\\\u0181\3\2\2\2^\u018f\3\2\2\2`\u0191")
        buf.write(u"\3\2\2\2b\u0195\3\2\2\2d\u0199\3\2\2\2f\u019d\3\2\2\2")
        buf.write(u"h\u01a0\3\2\2\2j\u01ad\3\2\2\2l\u01bf\3\2\2\2n\u01da")
        buf.write(u"\3\2\2\2p\u01dd\3\2\2\2r\u01e4\3\2\2\2t\u01e6\3\2\2\2")
        buf.write(u"v\u01f6\3\2\2\2x\u0207\3\2\2\2z\u0209\3\2\2\2|\u020b")
        buf.write(u"\3\2\2\2~\u020d\3\2\2\2\u0080\u020f\3\2\2\2\u0082\u0211")
        buf.write(u"\3\2\2\2\u0084\u0213\3\2\2\2\u0086\u0215\3\2\2\2\u0088")
        buf.write(u"\u0217\3\2\2\2\u008a\u0219\3\2\2\2\u008c\u021b\3\2\2")
        buf.write(u"\2\u008e\u021d\3\2\2\2\u0090\u0095\5\24\13\2\u0091\u0095")
        buf.write(u"\5\b\5\2\u0092\u0095\5\4\3\2\u0093\u0095\5:\36\2\u0094")
        buf.write(u"\u0090\3\2\2\2\u0094\u0091\3\2\2\2\u0094\u0092\3\2\2")
        buf.write(u"\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write(u"\3\2\2\2\u0096\u0097\3\2\2\2\u0097\3\3\2\2\2\u0098\u0096")
        buf.write(u"\3\2\2\2\u0099\u009a\7+\2\2\u009a\u009b\5(\25\2\u009b")
        buf.write(u"\u009c\5\6\4\2\u009c\5\3\2\2\2\u009d\u00a1\7\3\2\2\u009e")
        buf.write(u"\u00a0\5\24\13\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2")
        buf.write(u"\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4")
        buf.write(u"\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7\4\2\2\u00a5")
        buf.write(u"\7\3\2\2\2\u00a6\u00a7\7\64\2\2\u00a7\u00a8\5\n\6\2\u00a8")
        buf.write(u"\u00a9\5\16\b\2\u00a9\t\3\2\2\2\u00aa\u00ab\5\u008eH")
        buf.write(u"\2\u00ab\u00ad\7\5\2\2\u00ac\u00ae\5\20\t\2\u00ad\u00ac")
        buf.write(u"\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write(u"\u00b0\7\6\2\2\u00b0\u00b1\7\7\2\2\u00b1\u00b2\5\f\7")
        buf.write(u"\2\u00b2\13\3\2\2\2\u00b3\u00b6\5$\23\2\u00b4\u00b6\5")
        buf.write(u"\60\31\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write(u"\r\3\2\2\2\u00b7\u00bb\7\3\2\2\u00b8\u00ba\5<\37\2\u00b9")
        buf.write(u"\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2")
        buf.write(u"\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bb")
        buf.write(u"\3\2\2\2\u00be\u00bf\7\4\2\2\u00bf\17\3\2\2\2\u00c0\u00c1")
        buf.write(u"\5\22\n\2\u00c1\u00c2\7\b\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write(u"\u00c0\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2")
        buf.write(u"\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c5")
        buf.write(u"\3\2\2\2\u00c8\u00c9\5\22\n\2\u00c9\21\3\2\2\2\u00ca")
        buf.write(u"\u00cb\5\u008eH\2\u00cb\u00cc\7\7\2\2\u00cc\u00cd\5$")
        buf.write(u"\23\2\u00cd\23\3\2\2\2\u00ce\u00cf\5\26\f\2\u00cf\u00d0")
        buf.write(u"\7\t\2\2\u00d0\25\3\2\2\2\u00d1\u00d2\5$\23\2\u00d2\u00d5")
        buf.write(u"\5\u008eH\2\u00d3\u00d4\7\n\2\2\u00d4\u00d6\5l\67\2\u00d5")
        buf.write(u"\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\27\3\2\2\2\u00d7")
        buf.write(u"\u00d8\7\13\2\2\u00d8\u00d9\5\u008eH\2\u00d9\u00db\7")
        buf.write(u"\5\2\2\u00da\u00dc\5\32\16\2\u00db\u00da\3\2\2\2\u00db")
        buf.write(u"\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7\6\2")
        buf.write(u"\2\u00de\31\3\2\2\2\u00df\u00e0\5\34\17\2\u00e0\u00e1")
        buf.write(u"\7\b\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00df\3\2\2\2\u00e3")
        buf.write(u"\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2")
        buf.write(u"\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8")
        buf.write(u"\5\34\17\2\u00e8\33\3\2\2\2\u00e9\u00ea\5\u008eH\2\u00ea")
        buf.write(u"\u00eb\7\n\2\2\u00eb\u00ec\5l\67\2\u00ec\35\3\2\2\2\u00ed")
        buf.write(u"\u00ef\7\f\2\2\u00ee\u00f0\5 \21\2\u00ef\u00ee\3\2\2")
        buf.write(u"\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2")
        buf.write(u"\7\r\2\2\u00f2\37\3\2\2\2\u00f3\u00f8\5l\67\2\u00f4\u00f5")
        buf.write(u"\7\b\2\2\u00f5\u00f7\5l\67\2\u00f6\u00f4\3\2\2\2\u00f7")
        buf.write(u"\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2")
        buf.write(u"\2\u00f9!\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\7\65")
        buf.write(u"\2\2\u00fc\u00fd\7\t\2\2\u00fd#\3\2\2\2\u00fe\u0102\5")
        buf.write(u"&\24\2\u00ff\u0102\5\62\32\2\u0100\u0102\5(\25\2\u0101")
        buf.write(u"\u00fe\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2")
        buf.write(u"\2\u0102%\3\2\2\2\u0103\u0107\5*\26\2\u0104\u0107\5,")
        buf.write(u"\27\2\u0105\u0107\5.\30\2\u0106\u0103\3\2\2\2\u0106\u0104")
        buf.write(u"\3\2\2\2\u0106\u0105\3\2\2\2\u0107\'\3\2\2\2\u0108\u0109")
        buf.write(u"\7\66\2\2\u0109)\3\2\2\2\u010a\u010b\7(\2\2\u010b+\3")
        buf.write(u"\2\2\2\u010c\u010d\7)\2\2\u010d-\3\2\2\2\u010e\u010f")
        buf.write(u"\7\'\2\2\u010f/\3\2\2\2\u0110\u0111\7*\2\2\u0111\61\3")
        buf.write(u"\2\2\2\u0112\u0113\7\f\2\2\u0113\u0114\5\66\34\2\u0114")
        buf.write(u"\u0115\7\r\2\2\u0115\63\3\2\2\2\u0116\u0119\5&\24\2\u0117")
        buf.write(u"\u0119\5\62\32\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2")
        buf.write(u"\2\2\u0119\65\3\2\2\2\u011a\u011f\5\64\33\2\u011b\u011c")
        buf.write(u"\7\b\2\2\u011c\u011e\5\64\33\2\u011d\u011b\3\2\2\2\u011e")
        buf.write(u"\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2")
        buf.write(u"\2\u0120\67\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0126\7")
        buf.write(u"\3\2\2\u0123\u0125\5<\37\2\u0124\u0123\3\2\2\2\u0125")
        buf.write(u"\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2")
        buf.write(u"\2\u0127\u0129\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a")
        buf.write(u"\7\4\2\2\u012a9\3\2\2\2\u012b\u012c\58\35\2\u012c;\3")
        buf.write(u"\2\2\2\u012d\u013b\5:\36\2\u012e\u013b\5\24\13\2\u012f")
        buf.write(u"\u013b\5n8\2\u0130\u013b\5T+\2\u0131\u013b\5f\64\2\u0132")
        buf.write(u"\u013b\5L\'\2\u0133\u013b\5J&\2\u0134\u013b\5\"\22\2")
        buf.write(u"\u0135\u013b\5^\60\2\u0136\u013b\5Z.\2\u0137\u013b\5")
        buf.write(u"> \2\u0138\u013b\5B\"\2\u0139\u013b\5F$\2\u013a\u012d")
        buf.write(u"\3\2\2\2\u013a\u012e\3\2\2\2\u013a\u012f\3\2\2\2\u013a")
        buf.write(u"\u0130\3\2\2\2\u013a\u0131\3\2\2\2\u013a\u0132\3\2\2")
        buf.write(u"\2\u013a\u0133\3\2\2\2\u013a\u0134\3\2\2\2\u013a\u0135")
        buf.write(u"\3\2\2\2\u013a\u0136\3\2\2\2\u013a\u0137\3\2\2\2\u013a")
        buf.write(u"\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b=\3\2\2\2\u013c")
        buf.write(u"\u013d\5@!\2\u013d\u013e\7\t\2\2\u013e?\3\2\2\2\u013f")
        buf.write(u"\u0140\7\16\2\2\u0140A\3\2\2\2\u0141\u0142\5D#\2\u0142")
        buf.write(u"\u0143\7\t\2\2\u0143C\3\2\2\2\u0144\u0145\7\17\2\2\u0145")
        buf.write(u"E\3\2\2\2\u0146\u0147\5H%\2\u0147\u0148\7\t\2\2\u0148")
        buf.write(u"G\3\2\2\2\u0149\u014b\7\63\2\2\u014a\u014c\5l\67\2\u014b")
        buf.write(u"\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014cI\3\2\2\2\u014d")
        buf.write(u"\u014e\7\60\2\2\u014e\u014f\7\5\2\2\u014f\u0150\5l\67")
        buf.write(u"\2\u0150\u0151\7\6\2\2\u0151\u0152\58\35\2\u0152K\3\2")
        buf.write(u"\2\2\u0153\u0154\7/\2\2\u0154\u0155\7\5\2\2\u0155\u0156")
        buf.write(u"\5N(\2\u0156\u0157\7\t\2\2\u0157\u0158\5P)\2\u0158\u0159")
        buf.write(u"\7\t\2\2\u0159\u015a\5R*\2\u015a\u015b\7\6\2\2\u015b")
        buf.write(u"\u015c\58\35\2\u015cM\3\2\2\2\u015d\u0160\5p9\2\u015e")
        buf.write(u"\u0160\5\26\f\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2")
        buf.write(u"\2\u0160O\3\2\2\2\u0161\u0162\5l\67\2\u0162Q\3\2\2\2")
        buf.write(u"\u0163\u0166\5p9\2\u0164\u0166\5h\65\2\u0165\u0163\3")
        buf.write(u"\2\2\2\u0165\u0164\3\2\2\2\u0166S\3\2\2\2\u0167\u0168")
        buf.write(u"\7\61\2\2\u0168\u0169\7\5\2\2\u0169\u016a\5l\67\2\u016a")
        buf.write(u"\u016b\7\6\2\2\u016b\u016f\5:\36\2\u016c\u016e\5V,\2")
        buf.write(u"\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d")
        buf.write(u"\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0173\3\2\2\2\u0171")
        buf.write(u"\u016f\3\2\2\2\u0172\u0174\5X-\2\u0173\u0172\3\2\2\2")
        buf.write(u"\u0173\u0174\3\2\2\2\u0174U\3\2\2\2\u0175\u0176\7\62")
        buf.write(u"\2\2\u0176\u0177\7\5\2\2\u0177\u0178\5l\67\2\u0178\u0179")
        buf.write(u"\7\6\2\2\u0179\u017a\5:\36\2\u017aW\3\2\2\2\u017b\u017c")
        buf.write(u"\7.\2\2\u017c\u017d\5:\36\2\u017dY\3\2\2\2\u017e\u017f")
        buf.write(u"\5\\/\2\u017f\u0180\7\t\2\2\u0180[\3\2\2\2\u0181\u0182")
        buf.write(u"\7,\2\2\u0182\u0183\7\5\2\2\u0183\u0184\5j\66\2\u0184")
        buf.write(u"\u0185\7\6\2\2\u0185]\3\2\2\2\u0186\u0187\5`\61\2\u0187")
        buf.write(u"\u0188\7\t\2\2\u0188\u0190\3\2\2\2\u0189\u018a\5b\62")
        buf.write(u"\2\u018a\u018b\7\t\2\2\u018b\u0190\3\2\2\2\u018c\u018d")
        buf.write(u"\5d\63\2\u018d\u018e\7\t\2\2\u018e\u0190\3\2\2\2\u018f")
        buf.write(u"\u0186\3\2\2\2\u018f\u0189\3\2\2\2\u018f\u018c\3\2\2")
        buf.write(u"\2\u0190_\3\2\2\2\u0191\u0192\7\20\2\2\u0192\u0193\7")
        buf.write(u"\5\2\2\u0193\u0194\7\6\2\2\u0194a\3\2\2\2\u0195\u0196")
        buf.write(u"\7\21\2\2\u0196\u0197\7\5\2\2\u0197\u0198\7\6\2\2\u0198")
        buf.write(u"c\3\2\2\2\u0199\u019a\7\22\2\2\u019a\u019b\7\5\2\2\u019b")
        buf.write(u"\u019c\7\6\2\2\u019ce\3\2\2\2\u019d\u019e\5h\65\2\u019e")
        buf.write(u"\u019f\7\t\2\2\u019fg\3\2\2\2\u01a0\u01a1\5\u008eH\2")
        buf.write(u"\u01a1\u01a2\7\5\2\2\u01a2\u01a3\5j\66\2\u01a3\u01a4")
        buf.write(u"\7\6\2\2\u01a4i\3\2\2\2\u01a5\u01aa\5l\67\2\u01a6\u01a7")
        buf.write(u"\7\b\2\2\u01a7\u01a9\5l\67\2\u01a8\u01a6\3\2\2\2\u01a9")
        buf.write(u"\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2")
        buf.write(u"\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01a5")
        buf.write(u"\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aek\3\2\2\2\u01af\u01b0")
        buf.write(u"\b\67\1\2\u01b0\u01b1\5\u0080A\2\u01b1\u01b2\5l\67\20")
        buf.write(u"\u01b2\u01c0\3\2\2\2\u01b3\u01b4\7\5\2\2\u01b4\u01b5")
        buf.write(u"\5l\67\2\u01b5\u01b6\7\6\2\2\u01b6\u01c0\3\2\2\2\u01b7")
        buf.write(u"\u01c0\5h\65\2\u01b8\u01c0\5x=\2\u01b9\u01c0\5\36\20")
        buf.write(u"\2\u01ba\u01c0\5\30\r\2\u01bb\u01c0\5r:\2\u01bc\u01c0")
        buf.write(u"\5`\61\2\u01bd\u01c0\5b\62\2\u01be\u01c0\5d\63\2\u01bf")
        buf.write(u"\u01af\3\2\2\2\u01bf\u01b3\3\2\2\2\u01bf\u01b7\3\2\2")
        buf.write(u"\2\u01bf\u01b8\3\2\2\2\u01bf\u01b9\3\2\2\2\u01bf\u01ba")
        buf.write(u"\3\2\2\2\u01bf\u01bb\3\2\2\2\u01bf\u01bc\3\2\2\2\u01bf")
        buf.write(u"\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01d7\3\2\2")
        buf.write(u"\2\u01c1\u01c2\f\17\2\2\u01c2\u01c3\5\u0082B\2\u01c3")
        buf.write(u"\u01c4\5l\67\20\u01c4\u01d6\3\2\2\2\u01c5\u01c6\f\16")
        buf.write(u"\2\2\u01c6\u01c7\5\u0084C\2\u01c7\u01c8\5l\67\17\u01c8")
        buf.write(u"\u01d6\3\2\2\2\u01c9\u01ca\f\r\2\2\u01ca\u01cb\5\u0086")
        buf.write(u"D\2\u01cb\u01cc\5l\67\16\u01cc\u01d6\3\2\2\2\u01cd\u01ce")
        buf.write(u"\f\f\2\2\u01ce\u01cf\5\u0088E\2\u01cf\u01d0\5l\67\r\u01d0")
        buf.write(u"\u01d6\3\2\2\2\u01d1\u01d2\f\13\2\2\u01d2\u01d3\5\u008a")
        buf.write(u"F\2\u01d3\u01d4\5l\67\f\u01d4\u01d6\3\2\2\2\u01d5\u01c1")
        buf.write(u"\3\2\2\2\u01d5\u01c5\3\2\2\2\u01d5\u01c9\3\2\2\2\u01d5")
        buf.write(u"\u01cd\3\2\2\2\u01d5\u01d1\3\2\2\2\u01d6\u01d9\3\2\2")
        buf.write(u"\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8m\3\2")
        buf.write(u"\2\2\u01d9\u01d7\3\2\2\2\u01da\u01db\5p9\2\u01db\u01dc")
        buf.write(u"\7\t\2\2\u01dco\3\2\2\2\u01dd\u01de\5r:\2\u01de\u01df")
        buf.write(u"\5\u008cG\2\u01df\u01e0\5l\67\2\u01e0q\3\2\2\2\u01e1")
        buf.write(u"\u01e5\5\u008eH\2\u01e2\u01e5\5v<\2\u01e3\u01e5\5t;\2")
        buf.write(u"\u01e4\u01e1\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e3")
        buf.write(u"\3\2\2\2\u01e5s\3\2\2\2\u01e6\u01e7\b;\1\2\u01e7\u01e8")
        buf.write(u"\5\u008eH\2\u01e8\u01e9\7\f\2\2\u01e9\u01ea\5z>\2\u01ea")
        buf.write(u"\u01eb\7\r\2\2\u01eb\u01f3\3\2\2\2\u01ec\u01ed\f\4\2")
        buf.write(u"\2\u01ed\u01ee\7\f\2\2\u01ee\u01ef\5z>\2\u01ef\u01f0")
        buf.write(u"\7\r\2\2\u01f0\u01f2\3\2\2\2\u01f1\u01ec\3\2\2\2\u01f2")
        buf.write(u"\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2")
        buf.write(u"\2\u01f4u\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f7\b<")
        buf.write(u"\1\2\u01f7\u01f8\5\u008eH\2\u01f8\u0201\3\2\2\2\u01f9")
        buf.write(u"\u01fa\f\3\2\2\u01fa\u01fd\7\23\2\2\u01fb\u01fe\5\u008e")
        buf.write(u"H\2\u01fc\u01fe\5t;\2\u01fd\u01fb\3\2\2\2\u01fd\u01fc")
        buf.write(u"\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u01f9\3\2\2\2\u0200")
        buf.write(u"\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2")
        buf.write(u"\2\u0202w\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0208\5z")
        buf.write(u">\2\u0205\u0208\5|?\2\u0206\u0208\5~@\2\u0207\u0204\3")
        buf.write(u"\2\2\2\u0207\u0205\3\2\2\2\u0207\u0206\3\2\2\2\u0208")
        buf.write(u"y\3\2\2\2\u0209\u020a\79\2\2\u020a{\3\2\2\2\u020b\u020c")
        buf.write(u"\78\2\2\u020c}\3\2\2\2\u020d\u020e\7\67\2\2\u020e\177")
        buf.write(u"\3\2\2\2\u020f\u0210\t\2\2\2\u0210\u0081\3\2\2\2\u0211")
        buf.write(u"\u0212\t\3\2\2\u0212\u0083\3\2\2\2\u0213\u0214\t\4\2")
        buf.write(u"\2\u0214\u0085\3\2\2\2\u0215\u0216\t\5\2\2\u0216\u0087")
        buf.write(u"\3\2\2\2\u0217\u0218\t\6\2\2\u0218\u0089\3\2\2\2\u0219")
        buf.write(u"\u021a\t\7\2\2\u021a\u008b\3\2\2\2\u021b\u021c\t\b\2")
        buf.write(u"\2\u021c\u008d\3\2\2\2\u021d\u021e\7\66\2\2\u021e\u008f")
        buf.write(u"\3\2\2\2$\u0094\u0096\u00a1\u00ad\u00b5\u00bb\u00c5\u00d5")
        buf.write(u"\u00db\u00e4\u00ef\u00f8\u0101\u0106\u0118\u011f\u0126")
        buf.write(u"\u013a\u014b\u015f\u0165\u016f\u0173\u018f\u01aa\u01ad")
        buf.write(u"\u01bf\u01d5\u01d7\u01e4\u01f3\u01fd\u0201\u0207")
        return buf.getvalue()
		

class LLangParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"'('", u"')'", u"':'", 
                     u"','", u"';'", u"'='", u"'new'", u"'['", u"']'", u"'break'", 
                     u"'continue'", u"'readInt'", u"'readStr'", u"'readBool'", 
                     u"'.'", u"'-'", u"'!'", u"'*'", u"'/'", u"'%'", u"'+'", 
                     u"'>'", u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", 
                     u"'&&'", u"'||'", u"'*='", u"'/='", u"'%='", u"'+='", 
                     u"'-='", u"'Bool'", u"'Int'", u"'Str'", u"'None'", 
                     u"'record'", u"'writeln'", u"'readln'", u"'else'", 
                     u"'for'", u"'while'", u"'if'", u"'elif'", u"'return'", 
                     u"'fun'", u"'pass'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"BOOL", u"INT", u"STR", u"NONE", u"RECORD", 
                      u"WRITELN", u"READLN", u"ELSE", u"FOR", u"WHILE", 
                      u"IF", u"ELIF", u"RETURN", u"FUN", u"PASS", u"Identifier", 
                      u"BooleanLiteral", u"StringLiteral", u"IntegerLiteral", 
                      u"WS", u"COMMENT", u"LINE_COMMENT" ]

    RULE_programme = 0
    RULE_recordDeclaration = 1
    RULE_recordBody = 2
    RULE_functionDeclaration = 3
    RULE_functionSignature = 4
    RULE_functionReturnType = 5
    RULE_functionBody = 6
    RULE_functionParameterList = 7
    RULE_functionParameter = 8
    RULE_variableDeclarationStatement = 9
    RULE_variableDeclaration = 10
    RULE_recordInitializer = 11
    RULE_recordFieldInitializerList = 12
    RULE_recordFieldInitializer = 13
    RULE_cortegeInitializer = 14
    RULE_expressionList = 15
    RULE_passStatement = 16
    RULE_exprType = 17
    RULE_primitiveType = 18
    RULE_recordId = 19
    RULE_intType = 20
    RULE_strType = 21
    RULE_boolType = 22
    RULE_voidType = 23
    RULE_cortegeType = 24
    RULE_cortegeTypeUnit = 25
    RULE_cortegeTypeNonEmptyList = 26
    RULE_block = 27
    RULE_justBlock = 28
    RULE_statement = 29
    RULE_breakStatement = 30
    RULE_breaks = 31
    RULE_continueStatement = 32
    RULE_continues = 33
    RULE_returnStatement = 34
    RULE_returnExpr = 35
    RULE_whileStatement = 36
    RULE_forStatement = 37
    RULE_forInit = 38
    RULE_forCondition = 39
    RULE_forUpdate = 40
    RULE_ifStatement = 41
    RULE_elifBlock = 42
    RULE_elseBlock = 43
    RULE_writelnStatement = 44
    RULE_writelnCall = 45
    RULE_readlnStatement = 46
    RULE_readIntCall = 47
    RULE_readStrCall = 48
    RULE_readBoolCall = 49
    RULE_functionInvocationStatement = 50
    RULE_functionInvocation = 51
    RULE_argumentList = 52
    RULE_expression = 53
    RULE_assignmentStatement = 54
    RULE_assignment = 55
    RULE_leftHandSide = 56
    RULE_cortegeAccess = 57
    RULE_recordFieldAccess = 58
    RULE_literal = 59
    RULE_intLiteral = 60
    RULE_strLiteral = 61
    RULE_boolLiteral = 62
    RULE_unaryOperator = 63
    RULE_mulDivModOperator = 64
    RULE_addSubOperator = 65
    RULE_compareOperator = 66
    RULE_equalOrNotOperator = 67
    RULE_boolOperator = 68
    RULE_assignmentOperator = 69
    RULE_identifier = 70

    ruleNames =  [ u"programme", u"recordDeclaration", u"recordBody", u"functionDeclaration", 
                   u"functionSignature", u"functionReturnType", u"functionBody", 
                   u"functionParameterList", u"functionParameter", u"variableDeclarationStatement", 
                   u"variableDeclaration", u"recordInitializer", u"recordFieldInitializerList", 
                   u"recordFieldInitializer", u"cortegeInitializer", u"expressionList", 
                   u"passStatement", u"exprType", u"primitiveType", u"recordId", 
                   u"intType", u"strType", u"boolType", u"voidType", u"cortegeType", 
                   u"cortegeTypeUnit", u"cortegeTypeNonEmptyList", u"block", 
                   u"justBlock", u"statement", u"breakStatement", u"breaks", 
                   u"continueStatement", u"continues", u"returnStatement", 
                   u"returnExpr", u"whileStatement", u"forStatement", u"forInit", 
                   u"forCondition", u"forUpdate", u"ifStatement", u"elifBlock", 
                   u"elseBlock", u"writelnStatement", u"writelnCall", u"readlnStatement", 
                   u"readIntCall", u"readStrCall", u"readBoolCall", u"functionInvocationStatement", 
                   u"functionInvocation", u"argumentList", u"expression", 
                   u"assignmentStatement", u"assignment", u"leftHandSide", 
                   u"cortegeAccess", u"recordFieldAccess", u"literal", u"intLiteral", 
                   u"strLiteral", u"boolLiteral", u"unaryOperator", u"mulDivModOperator", 
                   u"addSubOperator", u"compareOperator", u"equalOrNotOperator", 
                   u"boolOperator", u"assignmentOperator", u"identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    BOOL=37
    INT=38
    STR=39
    NONE=40
    RECORD=41
    WRITELN=42
    READLN=43
    ELSE=44
    FOR=45
    WHILE=46
    IF=47
    ELIF=48
    RETURN=49
    FUN=50
    PASS=51
    Identifier=52
    BooleanLiteral=53
    StringLiteral=54
    IntegerLiteral=55
    WS=56
    COMMENT=57
    LINE_COMMENT=58

    def __init__(self, input):
        super(LLangParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgrammeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ProgrammeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationStatement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.VariableDeclarationStatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.VariableDeclarationStatementContext,i)


        def functionDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(LLangParser.FunctionDeclarationContext,i)


        def recordDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.RecordDeclarationContext)
            else:
                return self.getTypedRuleContext(LLangParser.RecordDeclarationContext,i)


        def justBlock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.JustBlockContext)
            else:
                return self.getTypedRuleContext(LLangParser.JustBlockContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_programme

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterProgramme(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitProgramme(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitProgramme(self)
            else:
                return visitor.visitChildren(self)




    def programme(self):

        localctx = LLangParser.ProgrammeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programme)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.RECORD) | (1 << LLangParser.FUN) | (1 << LLangParser.Identifier))) != 0):
                self.state = 146
                token = self._input.LA(1)
                if token in [LLangParser.T__9, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                    self.state = 142 
                    self.variableDeclarationStatement()

                elif token in [LLangParser.FUN]:
                    self.state = 143 
                    self.functionDeclaration()

                elif token in [LLangParser.RECORD]:
                    self.state = 144 
                    self.recordDeclaration()

                elif token in [LLangParser.T__0]:
                    self.state = 145 
                    self.justBlock()

                else:
                    raise NoViableAltException(self)

                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RECORD(self):
            return self.getToken(LLangParser.RECORD, 0)

        def recordId(self):
            return self.getTypedRuleContext(LLangParser.RecordIdContext,0)


        def recordBody(self):
            return self.getTypedRuleContext(LLangParser.RecordBodyContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordDeclaration

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def recordDeclaration(self):

        localctx = LLangParser.RecordDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_recordDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LLangParser.RECORD)
            self.state = 152 
            self.recordId()
            self.state = 153 
            self.recordBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationStatement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.VariableDeclarationStatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.VariableDeclarationStatementContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_recordBody

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordBody(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordBody(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordBody(self)
            else:
                return visitor.visitChildren(self)




    def recordBody(self):

        localctx = LLangParser.RecordBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_recordBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(LLangParser.T__0)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.Identifier))) != 0):
                self.state = 156 
                self.variableDeclarationStatement()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(LLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(LLangParser.FUN, 0)

        def functionSignature(self):
            return self.getTypedRuleContext(LLangParser.FunctionSignatureContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(LLangParser.FunctionBodyContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionDeclaration

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = LLangParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(LLangParser.FUN)
            self.state = 165 
            self.functionSignature()
            self.state = 166 
            self.functionBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionSignatureContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionSignatureContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def functionReturnType(self):
            return self.getTypedRuleContext(LLangParser.FunctionReturnTypeContext,0)


        def functionParameterList(self):
            return self.getTypedRuleContext(LLangParser.FunctionParameterListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionSignature

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionSignature(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionSignature(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionSignature(self)
            else:
                return visitor.visitChildren(self)




    def functionSignature(self):

        localctx = LLangParser.FunctionSignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168 
            self.identifier()
            self.state = 169
            self.match(LLangParser.T__2)
            self.state = 171
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 170 
                self.functionParameterList()


            self.state = 173
            self.match(LLangParser.T__3)
            self.state = 174
            self.match(LLangParser.T__4)
            self.state = 175 
            self.functionReturnType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionReturnTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exprType(self):
            return self.getTypedRuleContext(LLangParser.ExprTypeContext,0)


        def voidType(self):
            return self.getTypedRuleContext(LLangParser.VoidTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionReturnType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionReturnType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionReturnType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionReturnType(self)
            else:
                return visitor.visitChildren(self)




    def functionReturnType(self):

        localctx = LLangParser.FunctionReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionReturnType)
        try:
            self.state = 179
            token = self._input.LA(1)
            if token in [LLangParser.T__9, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177 
                self.exprType()

            elif token in [LLangParser.NONE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178 
                self.voidType()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.StatementContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_functionBody

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionBody(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = LLangParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(LLangParser.T__0)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.T__11) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.T__14) | (1 << LLangParser.T__15) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.RETURN) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 182 
                self.statement()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(LLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def functionParameter(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.FunctionParameterContext)
            else:
                return self.getTypedRuleContext(LLangParser.FunctionParameterContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_functionParameterList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionParameterList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionParameterList(self)
            else:
                return visitor.visitChildren(self)




    def functionParameterList(self):

        localctx = LLangParser.FunctionParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionParameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 190 
                    self.functionParameter()
                    self.state = 191
                    self.match(LLangParser.T__5) 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 198 
            self.functionParameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionParameterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionParameterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def exprType(self):
            return self.getTypedRuleContext(LLangParser.ExprTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionParameter

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionParameter(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionParameter(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionParameter(self)
            else:
                return visitor.visitChildren(self)




    def functionParameter(self):

        localctx = LLangParser.FunctionParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200 
            self.identifier()
            self.state = 201
            self.match(LLangParser.T__4)
            self.state = 202 
            self.exprType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableDeclarationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(LLangParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_variableDeclarationStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableDeclarationStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableDeclarationStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationStatement(self):

        localctx = LLangParser.VariableDeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variableDeclarationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204 
            self.variableDeclaration()
            self.state = 205
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exprType(self):
            return self.getTypedRuleContext(LLangParser.ExprTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_variableDeclaration

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = LLangParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207 
            self.exprType()
            self.state = 208 
            self.identifier()
            self.state = 211
            _la = self._input.LA(1)
            if _la==LLangParser.T__7:
                self.state = 209
                self.match(LLangParser.T__7)
                self.state = 210 
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def recordFieldInitializerList(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldInitializerListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordInitializer(self)
            else:
                return visitor.visitChildren(self)




    def recordInitializer(self):

        localctx = LLangParser.RecordInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_recordInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(LLangParser.T__8)
            self.state = 214 
            self.identifier()
            self.state = 215
            self.match(LLangParser.T__2)
            self.state = 217
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 216 
                self.recordFieldInitializerList()


            self.state = 219
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordFieldInitializerListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldInitializerListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def recordFieldInitializer(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.RecordFieldInitializerContext)
            else:
                return self.getTypedRuleContext(LLangParser.RecordFieldInitializerContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_recordFieldInitializerList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordFieldInitializerList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordFieldInitializerList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordFieldInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def recordFieldInitializerList(self):

        localctx = LLangParser.RecordFieldInitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_recordFieldInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 221 
                    self.recordFieldInitializer()
                    self.state = 222
                    self.match(LLangParser.T__5) 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 229 
            self.recordFieldInitializer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordFieldInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordFieldInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordFieldInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordFieldInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordFieldInitializer(self)
            else:
                return visitor.visitChildren(self)




    def recordFieldInitializer(self):

        localctx = LLangParser.RecordFieldInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_recordFieldInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231 
            self.identifier()
            self.state = 232
            self.match(LLangParser.T__7)
            self.state = 233 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(LLangParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeInitializer(self)
            else:
                return visitor.visitChildren(self)




    def cortegeInitializer(self):

        localctx = LLangParser.CortegeInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cortegeInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(LLangParser.T__9)
            self.state = 237
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__13) | (1 << LLangParser.T__14) | (1 << LLangParser.T__15) | (1 << LLangParser.T__17) | (1 << LLangParser.T__18) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 236 
                self.expressionList()


            self.state = 239
            self.match(LLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ExpressionListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_expressionList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterExpressionList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitExpressionList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = LLangParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241 
            self.expression(0)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 242
                self.match(LLangParser.T__5)
                self.state = 243 
                self.expression(0)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PassStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.PassStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PASS(self):
            return self.getToken(LLangParser.PASS, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_passStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterPassStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitPassStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitPassStatement(self)
            else:
                return visitor.visitChildren(self)




    def passStatement(self):

        localctx = LLangParser.PassStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_passStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(LLangParser.PASS)
            self.state = 250
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ExprTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(LLangParser.PrimitiveTypeContext,0)


        def cortegeType(self):
            return self.getTypedRuleContext(LLangParser.CortegeTypeContext,0)


        def recordId(self):
            return self.getTypedRuleContext(LLangParser.RecordIdContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_exprType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterExprType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitExprType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitExprType(self)
            else:
                return visitor.visitChildren(self)




    def exprType(self):

        localctx = LLangParser.ExprTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprType)
        try:
            self.state = 255
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252 
                self.primitiveType()

            elif token in [LLangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253 
                self.cortegeType()

            elif token in [LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 254 
                self.recordId()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimitiveTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.PrimitiveTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def intType(self):
            return self.getTypedRuleContext(LLangParser.IntTypeContext,0)


        def strType(self):
            return self.getTypedRuleContext(LLangParser.StrTypeContext,0)


        def boolType(self):
            return self.getTypedRuleContext(LLangParser.BoolTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_primitiveType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = LLangParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primitiveType)
        try:
            self.state = 260
            token = self._input.LA(1)
            if token in [LLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257 
                self.intType()

            elif token in [LLangParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258 
                self.strType()

            elif token in [LLangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 259 
                self.boolType()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordIdContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordIdContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(LLangParser.Identifier, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_recordId

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordId(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordId(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordId(self)
            else:
                return visitor.visitChildren(self)




    def recordId(self):

        localctx = LLangParser.RecordIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_recordId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(LLangParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IntTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LLangParser.INT, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_intType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIntType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIntType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)




    def intType(self):

        localctx = LLangParser.IntTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_intType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(LLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.StrTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(LLangParser.STR, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_strType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterStrType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitStrType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitStrType(self)
            else:
                return visitor.visitChildren(self)




    def strType(self):

        localctx = LLangParser.StrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_strType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(LLangParser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BoolTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(LLangParser.BOOL, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_boolType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBoolType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBoolType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBoolType(self)
            else:
                return visitor.visitChildren(self)




    def boolType(self):

        localctx = LLangParser.BoolTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_boolType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(LLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VoidTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VoidTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(LLangParser.NONE, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_voidType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVoidType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVoidType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVoidType(self)
            else:
                return visitor.visitChildren(self)




    def voidType(self):

        localctx = LLangParser.VoidTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_voidType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(LLangParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def cortegeTypeNonEmptyList(self):
            return self.getTypedRuleContext(LLangParser.CortegeTypeNonEmptyListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeType(self)
            else:
                return visitor.visitChildren(self)




    def cortegeType(self):

        localctx = LLangParser.CortegeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_cortegeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(LLangParser.T__9)
            self.state = 273 
            self.cortegeTypeNonEmptyList()
            self.state = 274
            self.match(LLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeTypeUnitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeTypeUnitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(LLangParser.PrimitiveTypeContext,0)


        def cortegeType(self):
            return self.getTypedRuleContext(LLangParser.CortegeTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeTypeUnit

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeTypeUnit(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeTypeUnit(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeTypeUnit(self)
            else:
                return visitor.visitChildren(self)




    def cortegeTypeUnit(self):

        localctx = LLangParser.CortegeTypeUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cortegeTypeUnit)
        try:
            self.state = 278
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276 
                self.primitiveType()

            elif token in [LLangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277 
                self.cortegeType()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeTypeNonEmptyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeTypeNonEmptyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def cortegeTypeUnit(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.CortegeTypeUnitContext)
            else:
                return self.getTypedRuleContext(LLangParser.CortegeTypeUnitContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeTypeNonEmptyList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeTypeNonEmptyList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeTypeNonEmptyList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeTypeNonEmptyList(self)
            else:
                return visitor.visitChildren(self)




    def cortegeTypeNonEmptyList(self):

        localctx = LLangParser.CortegeTypeNonEmptyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_cortegeTypeNonEmptyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280 
            self.cortegeTypeUnit()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 281
                self.match(LLangParser.T__5)
                self.state = 282 
                self.cortegeTypeUnit()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.StatementContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(LLangParser.T__0)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.T__11) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.T__14) | (1 << LLangParser.T__15) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.RETURN) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 289 
                self.statement()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self.match(LLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JustBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.JustBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_justBlock

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterJustBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitJustBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitJustBlock(self)
            else:
                return visitor.visitChildren(self)




    def justBlock(self):

        localctx = LLangParser.JustBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_justBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


        def variableDeclarationStatement(self):
            return self.getTypedRuleContext(LLangParser.VariableDeclarationStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(LLangParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(LLangParser.IfStatementContext,0)


        def functionInvocationStatement(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(LLangParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(LLangParser.WhileStatementContext,0)


        def passStatement(self):
            return self.getTypedRuleContext(LLangParser.PassStatementContext,0)


        def readlnStatement(self):
            return self.getTypedRuleContext(LLangParser.ReadlnStatementContext,0)


        def writelnStatement(self):
            return self.getTypedRuleContext(LLangParser.WritelnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(LLangParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(LLangParser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(LLangParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 312
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299 
                self.justBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300 
                self.variableDeclarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 301 
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 302 
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 303 
                self.functionInvocationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 304 
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 305 
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 306 
                self.passStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 307 
                self.readlnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 308 
                self.writelnStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 309 
                self.breakStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 310 
                self.continueStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 311 
                self.returnStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BreakStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def breaks(self):
            return self.getTypedRuleContext(LLangParser.BreaksContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_breakStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBreakStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = LLangParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314 
            self.breaks()
            self.state = 315
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreaksContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BreaksContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_breaks

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBreaks(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBreaks(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBreaks(self)
            else:
                return visitor.visitChildren(self)




    def breaks(self):

        localctx = LLangParser.BreaksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_breaks)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(LLangParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ContinueStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def continues(self):
            return self.getTypedRuleContext(LLangParser.ContinuesContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_continueStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitContinueStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = LLangParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319 
            self.continues()
            self.state = 320
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinuesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ContinuesContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_continues

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterContinues(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitContinues(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitContinues(self)
            else:
                return visitor.visitChildren(self)




    def continues(self):

        localctx = LLangParser.ContinuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_continues)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(LLangParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReturnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def returnExpr(self):
            return self.getTypedRuleContext(LLangParser.ReturnExprContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_returnStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReturnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = LLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324 
            self.returnExpr()
            self.state = 325
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReturnExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LLangParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_returnExpr

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReturnExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReturnExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReturnExpr(self)
            else:
                return visitor.visitChildren(self)




    def returnExpr(self):

        localctx = LLangParser.ReturnExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_returnExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(LLangParser.RETURN)
            self.state = 329
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__13) | (1 << LLangParser.T__14) | (1 << LLangParser.T__15) | (1 << LLangParser.T__17) | (1 << LLangParser.T__18) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 328 
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.WhileStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LLangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_whileStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitWhileStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = LLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(LLangParser.WHILE)
            self.state = 332
            self.match(LLangParser.T__2)
            self.state = 333 
            self.expression(0)
            self.state = 334
            self.match(LLangParser.T__3)
            self.state = 335 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ForStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LLangParser.FOR, 0)

        def forInit(self):
            return self.getTypedRuleContext(LLangParser.ForInitContext,0)


        def forCondition(self):
            return self.getTypedRuleContext(LLangParser.ForConditionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(LLangParser.ForUpdateContext,0)


        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_forStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitForStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = LLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(LLangParser.FOR)
            self.state = 338
            self.match(LLangParser.T__2)
            self.state = 339 
            self.forInit()
            self.state = 340
            self.match(LLangParser.T__6)
            self.state = 341 
            self.forCondition()
            self.state = 342
            self.match(LLangParser.T__6)
            self.state = 343 
            self.forUpdate()
            self.state = 344
            self.match(LLangParser.T__3)
            self.state = 345 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForInitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ForInitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(LLangParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_forInit

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterForInit(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitForInit(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = LLangParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_forInit)
        try:
            self.state = 349
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348 
                self.variableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForConditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ForConditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_forCondition

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterForCondition(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitForCondition(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = LLangParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForUpdateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ForUpdateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


        def functionInvocation(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_forUpdate

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterForUpdate(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitForUpdate(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = LLangParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forUpdate)
        try:
            self.state = 355
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354 
                self.functionInvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IfStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LLangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


        def elifBlock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ElifBlockContext)
            else:
                return self.getTypedRuleContext(LLangParser.ElifBlockContext,i)


        def elseBlock(self):
            return self.getTypedRuleContext(LLangParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_ifStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIfStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = LLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(LLangParser.IF)
            self.state = 358
            self.match(LLangParser.T__2)
            self.state = 359 
            self.expression(0)
            self.state = 360
            self.match(LLangParser.T__3)
            self.state = 361 
            self.justBlock()
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.ELIF:
                self.state = 362 
                self.elifBlock()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 369
            _la = self._input.LA(1)
            if _la==LLangParser.ELSE:
                self.state = 368 
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElifBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ElifBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(LLangParser.ELIF, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_elifBlock

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterElifBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitElifBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitElifBlock(self)
            else:
                return visitor.visitChildren(self)




    def elifBlock(self):

        localctx = LLangParser.ElifBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(LLangParser.ELIF)
            self.state = 372
            self.match(LLangParser.T__2)
            self.state = 373 
            self.expression(0)
            self.state = 374
            self.match(LLangParser.T__3)
            self.state = 375 
            self.justBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ElseBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(LLangParser.ELSE, 0)

        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_elseBlock

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterElseBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitElseBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = LLangParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(LLangParser.ELSE)
            self.state = 378 
            self.justBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WritelnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.WritelnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def writelnCall(self):
            return self.getTypedRuleContext(LLangParser.WritelnCallContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_writelnStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterWritelnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitWritelnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitWritelnStatement(self)
            else:
                return visitor.visitChildren(self)




    def writelnStatement(self):

        localctx = LLangParser.WritelnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_writelnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380 
            self.writelnCall()
            self.state = 381
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WritelnCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.WritelnCallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WRITELN(self):
            return self.getToken(LLangParser.WRITELN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(LLangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_writelnCall

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterWritelnCall(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitWritelnCall(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitWritelnCall(self)
            else:
                return visitor.visitChildren(self)




    def writelnCall(self):

        localctx = LLangParser.WritelnCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_writelnCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(LLangParser.WRITELN)
            self.state = 384
            self.match(LLangParser.T__2)
            self.state = 385 
            self.argumentList()
            self.state = 386
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadlnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReadlnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def readIntCall(self):
            return self.getTypedRuleContext(LLangParser.ReadIntCallContext,0)


        def readStrCall(self):
            return self.getTypedRuleContext(LLangParser.ReadStrCallContext,0)


        def readBoolCall(self):
            return self.getTypedRuleContext(LLangParser.ReadBoolCallContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_readlnStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReadlnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReadlnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReadlnStatement(self)
            else:
                return visitor.visitChildren(self)




    def readlnStatement(self):

        localctx = LLangParser.ReadlnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_readlnStatement)
        try:
            self.state = 397
            token = self._input.LA(1)
            if token in [LLangParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388 
                self.readIntCall()
                self.state = 389
                self.match(LLangParser.T__6)

            elif token in [LLangParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391 
                self.readStrCall()
                self.state = 392
                self.match(LLangParser.T__6)

            elif token in [LLangParser.T__15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 394 
                self.readBoolCall()
                self.state = 395
                self.match(LLangParser.T__6)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadIntCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReadIntCallContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_readIntCall

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReadIntCall(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReadIntCall(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReadIntCall(self)
            else:
                return visitor.visitChildren(self)




    def readIntCall(self):

        localctx = LLangParser.ReadIntCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_readIntCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(LLangParser.T__13)
            self.state = 400
            self.match(LLangParser.T__2)
            self.state = 401
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadStrCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReadStrCallContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_readStrCall

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReadStrCall(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReadStrCall(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReadStrCall(self)
            else:
                return visitor.visitChildren(self)




    def readStrCall(self):

        localctx = LLangParser.ReadStrCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_readStrCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(LLangParser.T__14)
            self.state = 404
            self.match(LLangParser.T__2)
            self.state = 405
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadBoolCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReadBoolCallContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_readBoolCall

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReadBoolCall(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReadBoolCall(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReadBoolCall(self)
            else:
                return visitor.visitChildren(self)




    def readBoolCall(self):

        localctx = LLangParser.ReadBoolCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_readBoolCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(LLangParser.T__15)
            self.state = 408
            self.match(LLangParser.T__2)
            self.state = 409
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionInvocationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionInvocationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def functionInvocation(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionInvocationStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionInvocationStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionInvocationStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionInvocationStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionInvocationStatement(self):

        localctx = LLangParser.FunctionInvocationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_functionInvocationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411 
            self.functionInvocation()
            self.state = 412
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionInvocationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(LLangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionInvocation

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionInvocation(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionInvocation(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionInvocation(self)
            else:
                return visitor.visitChildren(self)




    def functionInvocation(self):

        localctx = LLangParser.FunctionInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_functionInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414 
            self.identifier()
            self.state = 415
            self.match(LLangParser.T__2)
            self.state = 416 
            self.argumentList()
            self.state = 417
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ArgumentListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_argumentList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitArgumentList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = LLangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__13) | (1 << LLangParser.T__14) | (1 << LLangParser.T__15) | (1 << LLangParser.T__17) | (1 << LLangParser.T__18) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 419 
                self.expression(0)
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LLangParser.T__5:
                    self.state = 420
                    self.match(LLangParser.T__5)
                    self.state = 421 
                    self.expression(0)
                    self.state = 426
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unaryOperator(self):
            return self.getTypedRuleContext(LLangParser.UnaryOperatorContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def functionInvocation(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationContext,0)


        def literal(self):
            return self.getTypedRuleContext(LLangParser.LiteralContext,0)


        def cortegeInitializer(self):
            return self.getTypedRuleContext(LLangParser.CortegeInitializerContext,0)


        def recordInitializer(self):
            return self.getTypedRuleContext(LLangParser.RecordInitializerContext,0)


        def leftHandSide(self):
            return self.getTypedRuleContext(LLangParser.LeftHandSideContext,0)


        def readIntCall(self):
            return self.getTypedRuleContext(LLangParser.ReadIntCallContext,0)


        def readStrCall(self):
            return self.getTypedRuleContext(LLangParser.ReadStrCallContext,0)


        def readBoolCall(self):
            return self.getTypedRuleContext(LLangParser.ReadBoolCallContext,0)


        def mulDivModOperator(self):
            return self.getTypedRuleContext(LLangParser.MulDivModOperatorContext,0)


        def addSubOperator(self):
            return self.getTypedRuleContext(LLangParser.AddSubOperatorContext,0)


        def compareOperator(self):
            return self.getTypedRuleContext(LLangParser.CompareOperatorContext,0)


        def equalOrNotOperator(self):
            return self.getTypedRuleContext(LLangParser.EqualOrNotOperatorContext,0)


        def boolOperator(self):
            return self.getTypedRuleContext(LLangParser.BoolOperatorContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_expression

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 430 
                self.unaryOperator()
                self.state = 431 
                self.expression(14)
                pass

            elif la_ == 2:
                self.state = 433
                self.match(LLangParser.T__2)
                self.state = 434 
                self.expression(0)
                self.state = 435
                self.match(LLangParser.T__3)
                pass

            elif la_ == 3:
                self.state = 437 
                self.functionInvocation()
                pass

            elif la_ == 4:
                self.state = 438 
                self.literal()
                pass

            elif la_ == 5:
                self.state = 439 
                self.cortegeInitializer()
                pass

            elif la_ == 6:
                self.state = 440 
                self.recordInitializer()
                pass

            elif la_ == 7:
                self.state = 441 
                self.leftHandSide()
                pass

            elif la_ == 8:
                self.state = 442 
                self.readIntCall()
                pass

            elif la_ == 9:
                self.state = 443 
                self.readStrCall()
                pass

            elif la_ == 10:
                self.state = 444 
                self.readBoolCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 469
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 467
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 447
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 448 
                        self.mulDivModOperator()
                        self.state = 449 
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 451
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 452 
                        self.addSubOperator()
                        self.state = 453 
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 455
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 456 
                        self.compareOperator()
                        self.state = 457 
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 459
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 460 
                        self.equalOrNotOperator()
                        self.state = 461 
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 463
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 464 
                        self.boolOperator()
                        self.state = 465 
                        self.expression(10)
                        pass

             
                self.state = 471
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignmentStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AssignmentStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_assignmentStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = LLangParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472 
            self.assignment()
            self.state = 473
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def leftHandSide(self):
            return self.getTypedRuleContext(LLangParser.LeftHandSideContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(LLangParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_assignment

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAssignment(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAssignment(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475 
            self.leftHandSide()
            self.state = 476 
            self.assignmentOperator()
            self.state = 477 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LeftHandSideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.LeftHandSideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def recordFieldAccess(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldAccessContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_leftHandSide

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterLeftHandSide(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitLeftHandSide(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitLeftHandSide(self)
            else:
                return visitor.visitChildren(self)




    def leftHandSide(self):

        localctx = LLangParser.LeftHandSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_leftHandSide)
        try:
            self.state = 482
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479 
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480 
                self.recordFieldAccess(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 481 
                self.cortegeAccess(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeAccessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeAccessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def intLiteral(self):
            return self.getTypedRuleContext(LLangParser.IntLiteralContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeAccess

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeAccess(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeAccess(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeAccess(self)
            else:
                return visitor.visitChildren(self)



    def cortegeAccess(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LLangParser.CortegeAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_cortegeAccess, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485 
            self.identifier()
            self.state = 486
            self.match(LLangParser.T__9)
            self.state = 487 
            self.intLiteral()
            self.state = 488
            self.match(LLangParser.T__10)
            self._ctx.stop = self._input.LT(-1)
            self.state = 497
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LLangParser.CortegeAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cortegeAccess)
                    self.state = 490
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 491
                    self.match(LLangParser.T__9)
                    self.state = 492 
                    self.intLiteral()
                    self.state = 493
                    self.match(LLangParser.T__10) 
                self.state = 499
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RecordFieldAccessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldAccessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def recordFieldAccess(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldAccessContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordFieldAccess

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordFieldAccess(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordFieldAccess(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordFieldAccess(self)
            else:
                return visitor.visitChildren(self)



    def recordFieldAccess(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LLangParser.RecordFieldAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_recordFieldAccess, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501 
            self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LLangParser.RecordFieldAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_recordFieldAccess)
                    self.state = 503
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 504
                    self.match(LLangParser.T__16)
                    self.state = 507
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        self.state = 505 
                        self.identifier()
                        pass

                    elif la_ == 2:
                        self.state = 506 
                        self.cortegeAccess(0)
                        pass

             
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def intLiteral(self):
            return self.getTypedRuleContext(LLangParser.IntLiteralContext,0)


        def strLiteral(self):
            return self.getTypedRuleContext(LLangParser.StrLiteralContext,0)


        def boolLiteral(self):
            return self.getTypedRuleContext(LLangParser.BoolLiteralContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_literal

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_literal)
        try:
            self.state = 517
            token = self._input.LA(1)
            if token in [LLangParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514 
                self.intLiteral()

            elif token in [LLangParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515 
                self.strLiteral()

            elif token in [LLangParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 516 
                self.boolLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IntLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(LLangParser.IntegerLiteral, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_intLiteral

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIntLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)




    def intLiteral(self):

        localctx = LLangParser.IntLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(LLangParser.IntegerLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.StrLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(LLangParser.StringLiteral, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_strLiteral

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterStrLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitStrLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitStrLiteral(self)
            else:
                return visitor.visitChildren(self)




    def strLiteral(self):

        localctx = LLangParser.StrLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_strLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(LLangParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BoolLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BooleanLiteral(self):
            return self.getToken(LLangParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_boolLiteral

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)




    def boolLiteral(self):

        localctx = LLangParser.BoolLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_boolLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(LLangParser.BooleanLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.UnaryOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_unaryOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitUnaryOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitUnaryOperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryOperator(self):

        localctx = LLangParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__17 or _la==LLangParser.T__18):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulDivModOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.MulDivModOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_mulDivModOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterMulDivModOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitMulDivModOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitMulDivModOperator(self)
            else:
                return visitor.visitChildren(self)




    def mulDivModOperator(self):

        localctx = LLangParser.MulDivModOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_mulDivModOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__19) | (1 << LLangParser.T__20) | (1 << LLangParser.T__21))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddSubOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AddSubOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_addSubOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAddSubOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAddSubOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAddSubOperator(self)
            else:
                return visitor.visitChildren(self)




    def addSubOperator(self):

        localctx = LLangParser.AddSubOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_addSubOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__17 or _la==LLangParser.T__22):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompareOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CompareOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_compareOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCompareOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCompareOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCompareOperator(self)
            else:
                return visitor.visitChildren(self)




    def compareOperator(self):

        localctx = LLangParser.CompareOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_compareOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__23) | (1 << LLangParser.T__24) | (1 << LLangParser.T__25) | (1 << LLangParser.T__26))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EqualOrNotOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.EqualOrNotOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_equalOrNotOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterEqualOrNotOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitEqualOrNotOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitEqualOrNotOperator(self)
            else:
                return visitor.visitChildren(self)




    def equalOrNotOperator(self):

        localctx = LLangParser.EqualOrNotOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_equalOrNotOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__27 or _la==LLangParser.T__28):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BoolOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_boolOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBoolOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBoolOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBoolOperator(self)
            else:
                return visitor.visitChildren(self)




    def boolOperator(self):

        localctx = LLangParser.BoolOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_boolOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__29 or _la==LLangParser.T__30):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AssignmentOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_assignmentOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = LLangParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__7) | (1 << LLangParser.T__31) | (1 << LLangParser.T__32) | (1 << LLangParser.T__33) | (1 << LLangParser.T__34) | (1 << LLangParser.T__35))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(LLangParser.Identifier, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_identifier

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIdentifier(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = LLangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(LLangParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[53] = self.expression_sempred
        self._predicates[57] = self.cortegeAccess_sempred
        self._predicates[58] = self.recordFieldAccess_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

    def cortegeAccess_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def recordFieldAccess_sempred(self, localctx, predIndex):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         



