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
        buf.write(u"\67\u01dd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\7\2~\n\2\f\2")
        buf.write(u"\16\2\u0081\13\2\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u0089\n")
        buf.write(u"\4\f\4\16\4\u008c\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write(u"\6\3\6\5\6\u0097\n\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7\u009f")
        buf.write(u"\n\7\3\b\3\b\7\b\u00a3\n\b\f\b\16\b\u00a6\13\b\3\b\5")
        buf.write(u"\b\u00a9\n\b\3\b\3\b\3\t\3\t\3\t\7\t\u00b0\n\t\f\t\16")
        buf.write(u"\t\u00b3\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write(u"\3\f\3\f\3\f\3\f\5\f\u00c2\n\f\3\r\3\r\5\r\u00c6\n\r")
        buf.write(u"\3\16\3\16\3\16\5\16\u00cb\n\16\3\16\3\16\3\17\3\17\3")
        buf.write(u"\17\7\17\u00d2\n\17\f\17\16\17\u00d5\13\17\3\17\3\17")
        buf.write(u"\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u00df\n\21\3\21\3")
        buf.write(u"\21\3\22\3\22\3\22\7\22\u00e6\n\22\f\22\16\22\u00e9\13")
        buf.write(u"\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00f1\n\24\3\25")
        buf.write(u"\3\25\3\25\5\25\u00f6\n\25\3\26\3\26\3\27\3\27\3\30\3")
        buf.write(u"\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write(u"\3\34\7\34\u0109\n\34\f\34\16\34\u010c\13\34\3\35\3\35")
        buf.write(u"\7\35\u0110\n\35\f\35\16\35\u0113\13\35\3\35\3\35\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0121")
        buf.write(u"\n\36\3\37\3\37\5\37\u0125\n\37\3\37\3\37\3 \3 \3 \3")
        buf.write(u" \3 \3 \3!\3!\3!\5!\u0132\n!\3!\3!\5!\u0136\n!\3!\3!")
        buf.write(u"\5!\u013a\n!\3!\3!\3!\3\"\3\"\5\"\u0141\n\"\3#\3#\5#")
        buf.write(u"\u0145\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u0152\n")
        buf.write(u"$\f$\16$\u0155\13$\3$\3$\5$\u0159\n$\3%\3%\3%\3&\3&\3")
        buf.write(u"&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\7(\u016b\n(\f(\16")
        buf.write(u"(\u016e\13(\3(\3(\3)\3)\3)\3*\3*\3*\5*\u0178\n*\3*\3")
        buf.write(u"*\3+\3+\3+\7+\u017f\n+\f+\16+\u0182\13+\3,\3,\3,\3,\3")
        buf.write(u",\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0192\n,\3,\3,\3,\3,")
        buf.write(u"\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\7,\u01a8")
        buf.write(u"\n,\f,\16,\u01ab\13,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\5")
        buf.write(u"/\u01b7\n/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write(u"\61\3\62\3\62\3\62\5\62\u01c5\n\62\3\63\3\63\3\64\3\64")
        buf.write(u"\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(u";\3<\3<\3=\3=\3=\2\3V>\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write(u"\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`")
        buf.write(u"bdfhjlnprtvx\2\t\4\2\36\36\'\'\3\2(*\3\2&\'\4\2\34\35")
        buf.write(u"!\"\4\2  ##\3\2$%\5\2\33\33+.\60\60\u01d9\2\177\3\2\2")
        buf.write(u"\2\4\u0082\3\2\2\2\6\u0086\3\2\2\2\b\u008f\3\2\2\2\n")
        buf.write(u"\u0093\3\2\2\2\f\u009e\3\2\2\2\16\u00a0\3\2\2\2\20\u00b1")
        buf.write(u"\3\2\2\2\22\u00b6\3\2\2\2\24\u00ba\3\2\2\2\26\u00bd\3")
        buf.write(u"\2\2\2\30\u00c5\3\2\2\2\32\u00c7\3\2\2\2\34\u00d3\3\2")
        buf.write(u"\2\2\36\u00d8\3\2\2\2 \u00dc\3\2\2\2\"\u00e2\3\2\2\2")
        buf.write(u"$\u00ea\3\2\2\2&\u00f0\3\2\2\2(\u00f5\3\2\2\2*\u00f7")
        buf.write(u"\3\2\2\2,\u00f9\3\2\2\2.\u00fb\3\2\2\2\60\u00fd\3\2\2")
        buf.write(u"\2\62\u00ff\3\2\2\2\64\u0101\3\2\2\2\66\u0105\3\2\2\2")
        buf.write(u"8\u010d\3\2\2\2:\u0120\3\2\2\2<\u0122\3\2\2\2>\u0128")
        buf.write(u"\3\2\2\2@\u012e\3\2\2\2B\u0140\3\2\2\2D\u0144\3\2\2\2")
        buf.write(u"F\u0146\3\2\2\2H\u015a\3\2\2\2J\u015d\3\2\2\2L\u0162")
        buf.write(u"\3\2\2\2N\u0165\3\2\2\2P\u0171\3\2\2\2R\u0174\3\2\2\2")
        buf.write(u"T\u017b\3\2\2\2V\u0191\3\2\2\2X\u01ac\3\2\2\2Z\u01af")
        buf.write(u"\3\2\2\2\\\u01b6\3\2\2\2^\u01b8\3\2\2\2`\u01bd\3\2\2")
        buf.write(u"\2b\u01c4\3\2\2\2d\u01c6\3\2\2\2f\u01c8\3\2\2\2h\u01ca")
        buf.write(u"\3\2\2\2j\u01cc\3\2\2\2l\u01ce\3\2\2\2n\u01d0\3\2\2\2")
        buf.write(u"p\u01d2\3\2\2\2r\u01d4\3\2\2\2t\u01d6\3\2\2\2v\u01d8")
        buf.write(u"\3\2\2\2x\u01da\3\2\2\2z~\5\24\13\2{~\5\b\5\2|~\5\4\3")
        buf.write(u"\2}z\3\2\2\2}{\3\2\2\2}|\3\2\2\2~\u0081\3\2\2\2\177}")
        buf.write(u"\3\2\2\2\177\u0080\3\2\2\2\u0080\3\3\2\2\2\u0081\177")
        buf.write(u"\3\2\2\2\u0082\u0083\7\7\2\2\u0083\u0084\5x=\2\u0084")
        buf.write(u"\u0085\5\6\4\2\u0085\5\3\2\2\2\u0086\u008a\7\24\2\2\u0087")
        buf.write(u"\u0089\5\24\13\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2")
        buf.write(u"\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d")
        buf.write(u"\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e\7\25\2\2\u008e")
        buf.write(u"\7\3\2\2\2\u008f\u0090\7\20\2\2\u0090\u0091\5\n\6\2\u0091")
        buf.write(u"\u0092\5\16\b\2\u0092\t\3\2\2\2\u0093\u0094\5x=\2\u0094")
        buf.write(u"\u0096\7\22\2\2\u0095\u0097\5\20\t\2\u0096\u0095\3\2")
        buf.write(u"\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write(u"\7\23\2\2\u0099\u009a\7\37\2\2\u009a\u009b\5\f\7\2\u009b")
        buf.write(u"\13\3\2\2\2\u009c\u009f\5&\24\2\u009d\u009f\5\62\32\2")
        buf.write(u"\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\r\3\2")
        buf.write(u"\2\2\u00a0\u00a4\7\24\2\2\u00a1\u00a3\5:\36\2\u00a2\u00a1")
        buf.write(u"\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write(u"\u00a5\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2")
        buf.write(u"\2\u00a7\u00a9\5<\37\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9")
        buf.write(u"\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7\25\2\2\u00ab")
        buf.write(u"\17\3\2\2\2\u00ac\u00ad\5\22\n\2\u00ad\u00ae\7\31\2\2")
        buf.write(u"\u00ae\u00b0\3\2\2\2\u00af\u00ac\3\2\2\2\u00b0\u00b3")
        buf.write(u"\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write(u"\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\5\22\n")
        buf.write(u"\2\u00b5\21\3\2\2\2\u00b6\u00b7\5x=\2\u00b7\u00b8\7\37")
        buf.write(u"\2\2\u00b8\u00b9\5&\24\2\u00b9\23\3\2\2\2\u00ba\u00bb")
        buf.write(u"\5\26\f\2\u00bb\u00bc\7\30\2\2\u00bc\25\3\2\2\2\u00bd")
        buf.write(u"\u00be\5&\24\2\u00be\u00c1\5x=\2\u00bf\u00c0\7\33\2\2")
        buf.write(u"\u00c0\u00c2\5\30\r\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write(u"\3\2\2\2\u00c2\27\3\2\2\2\u00c3\u00c6\5V,\2\u00c4\u00c6")
        buf.write(u"\5 \21\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write(u"\31\3\2\2\2\u00c7\u00c8\5x=\2\u00c8\u00ca\7\22\2\2\u00c9")
        buf.write(u"\u00cb\5\34\17\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2")
        buf.write(u"\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\7\23\2\2\u00cd\33")
        buf.write(u"\3\2\2\2\u00ce\u00cf\5\36\20\2\u00cf\u00d0\7\31\2\2\u00d0")
        buf.write(u"\u00d2\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d2\u00d5\3\2\2")
        buf.write(u"\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6")
        buf.write(u"\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\5\36\20\2\u00d7")
        buf.write(u"\35\3\2\2\2\u00d8\u00d9\5x=\2\u00d9\u00da\7\33\2\2\u00da")
        buf.write(u"\u00db\5V,\2\u00db\37\3\2\2\2\u00dc\u00de\7\26\2\2\u00dd")
        buf.write(u"\u00df\5\"\22\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2")
        buf.write(u"\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\7\27\2\2\u00e1!\3")
        buf.write(u"\2\2\2\u00e2\u00e7\5\30\r\2\u00e3\u00e4\7\31\2\2\u00e4")
        buf.write(u"\u00e6\5\30\r\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9\3\2\2")
        buf.write(u"\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8#\3\2")
        buf.write(u"\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\7\21\2\2\u00eb\u00ec")
        buf.write(u"\7\30\2\2\u00ec%\3\2\2\2\u00ed\u00f1\5(\25\2\u00ee\u00f1")
        buf.write(u"\5\64\33\2\u00ef\u00f1\5*\26\2\u00f0\u00ed\3\2\2\2\u00f0")
        buf.write(u"\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\'\3\2\2\2\u00f2")
        buf.write(u"\u00f6\5,\27\2\u00f3\u00f6\5.\30\2\u00f4\u00f6\5\60\31")
        buf.write(u"\2\u00f5\u00f2\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4")
        buf.write(u"\3\2\2\2\u00f6)\3\2\2\2\u00f7\u00f8\7\61\2\2\u00f8+\3")
        buf.write(u"\2\2\2\u00f9\u00fa\7\4\2\2\u00fa-\3\2\2\2\u00fb\u00fc")
        buf.write(u"\7\5\2\2\u00fc/\3\2\2\2\u00fd\u00fe\7\3\2\2\u00fe\61")
        buf.write(u"\3\2\2\2\u00ff\u0100\7\6\2\2\u0100\63\3\2\2\2\u0101\u0102")
        buf.write(u"\7\26\2\2\u0102\u0103\5\66\34\2\u0103\u0104\7\27\2\2")
        buf.write(u"\u0104\65\3\2\2\2\u0105\u010a\5&\24\2\u0106\u0107\7\31")
        buf.write(u"\2\2\u0107\u0109\5&\24\2\u0108\u0106\3\2\2\2\u0109\u010c")
        buf.write(u"\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write(u"\67\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u0111\7\24\2\2")
        buf.write(u"\u010e\u0110\5:\36\2\u010f\u010e\3\2\2\2\u0110\u0113")
        buf.write(u"\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write(u"\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\7\25\2")
        buf.write(u"\2\u01159\3\2\2\2\u0116\u0121\58\35\2\u0117\u0121\5\24")
        buf.write(u"\13\2\u0118\u0121\5X-\2\u0119\u0121\5F$\2\u011a\u0121")
        buf.write(u"\5P)\2\u011b\u0121\5@!\2\u011c\u0121\5> \2\u011d\u0121")
        buf.write(u"\5$\23\2\u011e\u0121\5L\'\2\u011f\u0121\5H%\2\u0120\u0116")
        buf.write(u"\3\2\2\2\u0120\u0117\3\2\2\2\u0120\u0118\3\2\2\2\u0120")
        buf.write(u"\u0119\3\2\2\2\u0120\u011a\3\2\2\2\u0120\u011b\3\2\2")
        buf.write(u"\2\u0120\u011c\3\2\2\2\u0120\u011d\3\2\2\2\u0120\u011e")
        buf.write(u"\3\2\2\2\u0120\u011f\3\2\2\2\u0121;\3\2\2\2\u0122\u0124")
        buf.write(u"\7\17\2\2\u0123\u0125\5V,\2\u0124\u0123\3\2\2\2\u0124")
        buf.write(u"\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\7\30\2")
        buf.write(u"\2\u0127=\3\2\2\2\u0128\u0129\7\f\2\2\u0129\u012a\7\22")
        buf.write(u"\2\2\u012a\u012b\5V,\2\u012b\u012c\7\23\2\2\u012c\u012d")
        buf.write(u"\58\35\2\u012d?\3\2\2\2\u012e\u012f\7\13\2\2\u012f\u0131")
        buf.write(u"\7\22\2\2\u0130\u0132\5B\"\2\u0131\u0130\3\2\2\2\u0131")
        buf.write(u"\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\7\30\2")
        buf.write(u"\2\u0134\u0136\5V,\2\u0135\u0134\3\2\2\2\u0135\u0136")
        buf.write(u"\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\7\30\2\2\u0138")
        buf.write(u"\u013a\5D#\2\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write(u"\u013a\u013b\3\2\2\2\u013b\u013c\7\23\2\2\u013c\u013d")
        buf.write(u"\58\35\2\u013dA\3\2\2\2\u013e\u0141\5Z.\2\u013f\u0141")
        buf.write(u"\5\26\f\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141")
        buf.write(u"C\3\2\2\2\u0142\u0145\5Z.\2\u0143\u0145\5R*\2\u0144\u0142")
        buf.write(u"\3\2\2\2\u0144\u0143\3\2\2\2\u0145E\3\2\2\2\u0146\u0147")
        buf.write(u"\7\r\2\2\u0147\u0148\7\22\2\2\u0148\u0149\5V,\2\u0149")
        buf.write(u"\u014a\7\23\2\2\u014a\u0153\58\35\2\u014b\u014c\7\16")
        buf.write(u"\2\2\u014c\u014d\7\22\2\2\u014d\u014e\5V,\2\u014e\u014f")
        buf.write(u"\7\23\2\2\u014f\u0150\58\35\2\u0150\u0152\3\2\2\2\u0151")
        buf.write(u"\u014b\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2")
        buf.write(u"\2\u0153\u0154\3\2\2\2\u0154\u0158\3\2\2\2\u0155\u0153")
        buf.write(u"\3\2\2\2\u0156\u0157\7\n\2\2\u0157\u0159\58\35\2\u0158")
        buf.write(u"\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159G\3\2\2\2\u015a")
        buf.write(u"\u015b\5J&\2\u015b\u015c\7\30\2\2\u015cI\3\2\2\2\u015d")
        buf.write(u"\u015e\7\b\2\2\u015e\u015f\7\22\2\2\u015f\u0160\5T+\2")
        buf.write(u"\u0160\u0161\7\23\2\2\u0161K\3\2\2\2\u0162\u0163\5N(")
        buf.write(u"\2\u0163\u0164\7\30\2\2\u0164M\3\2\2\2\u0165\u0166\7")
        buf.write(u"\t\2\2\u0166\u0167\7\22\2\2\u0167\u016c\5\\/\2\u0168")
        buf.write(u"\u0169\7\31\2\2\u0169\u016b\5\\/\2\u016a\u0168\3\2\2")
        buf.write(u"\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write(u"\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f")
        buf.write(u"\u0170\7\23\2\2\u0170O\3\2\2\2\u0171\u0172\5R*\2\u0172")
        buf.write(u"\u0173\7\30\2\2\u0173Q\3\2\2\2\u0174\u0175\5x=\2\u0175")
        buf.write(u"\u0177\7\22\2\2\u0176\u0178\5T+\2\u0177\u0176\3\2\2\2")
        buf.write(u"\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a")
        buf.write(u"\7\23\2\2\u017aS\3\2\2\2\u017b\u0180\5V,\2\u017c\u017d")
        buf.write(u"\7\31\2\2\u017d\u017f\5V,\2\u017e\u017c\3\2\2\2\u017f")
        buf.write(u"\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2")
        buf.write(u"\2\u0181U\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184\b,")
        buf.write(u"\1\2\u0184\u0185\5j\66\2\u0185\u0186\5V,\16\u0186\u0192")
        buf.write(u"\3\2\2\2\u0187\u0192\5Z.\2\u0188\u0192\5R*\2\u0189\u0192")
        buf.write(u"\5b\62\2\u018a\u0192\5 \21\2\u018b\u0192\5\32\16\2\u018c")
        buf.write(u"\u0192\5\\/\2\u018d\u018e\7\22\2\2\u018e\u018f\5V,\2")
        buf.write(u"\u018f\u0190\7\23\2\2\u0190\u0192\3\2\2\2\u0191\u0183")
        buf.write(u"\3\2\2\2\u0191\u0187\3\2\2\2\u0191\u0188\3\2\2\2\u0191")
        buf.write(u"\u0189\3\2\2\2\u0191\u018a\3\2\2\2\u0191\u018b\3\2\2")
        buf.write(u"\2\u0191\u018c\3\2\2\2\u0191\u018d\3\2\2\2\u0192\u01a9")
        buf.write(u"\3\2\2\2\u0193\u0194\f\r\2\2\u0194\u0195\5l\67\2\u0195")
        buf.write(u"\u0196\5V,\16\u0196\u01a8\3\2\2\2\u0197\u0198\f\f\2\2")
        buf.write(u"\u0198\u0199\5n8\2\u0199\u019a\5V,\r\u019a\u01a8\3\2")
        buf.write(u"\2\2\u019b\u019c\f\13\2\2\u019c\u019d\5p9\2\u019d\u019e")
        buf.write(u"\5V,\f\u019e\u01a8\3\2\2\2\u019f\u01a0\f\n\2\2\u01a0")
        buf.write(u"\u01a1\5r:\2\u01a1\u01a2\5V,\13\u01a2\u01a8\3\2\2\2\u01a3")
        buf.write(u"\u01a4\f\t\2\2\u01a4\u01a5\5t;\2\u01a5\u01a6\5V,\n\u01a6")
        buf.write(u"\u01a8\3\2\2\2\u01a7\u0193\3\2\2\2\u01a7\u0197\3\2\2")
        buf.write(u"\2\u01a7\u019b\3\2\2\2\u01a7\u019f\3\2\2\2\u01a7\u01a3")
        buf.write(u"\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write(u"\u01aa\3\2\2\2\u01aaW\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write(u"\u01ad\5Z.\2\u01ad\u01ae\7\30\2\2\u01aeY\3\2\2\2\u01af")
        buf.write(u"\u01b0\5\\/\2\u01b0\u01b1\5v<\2\u01b1\u01b2\5V,\2\u01b2")
        buf.write(u"[\3\2\2\2\u01b3\u01b7\5x=\2\u01b4\u01b7\5^\60\2\u01b5")
        buf.write(u"\u01b7\5`\61\2\u01b6\u01b3\3\2\2\2\u01b6\u01b4\3\2\2")
        buf.write(u"\2\u01b6\u01b5\3\2\2\2\u01b7]\3\2\2\2\u01b8\u01b9\5x")
        buf.write(u"=\2\u01b9\u01ba\7\26\2\2\u01ba\u01bb\5V,\2\u01bb\u01bc")
        buf.write(u"\7\27\2\2\u01bc_\3\2\2\2\u01bd\u01be\5x=\2\u01be\u01bf")
        buf.write(u"\7\32\2\2\u01bf\u01c0\5\\/\2\u01c0a\3\2\2\2\u01c1\u01c5")
        buf.write(u"\5d\63\2\u01c2\u01c5\5f\64\2\u01c3\u01c5\5h\65\2\u01c4")
        buf.write(u"\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2")
        buf.write(u"\2\u01c5c\3\2\2\2\u01c6\u01c7\7\64\2\2\u01c7e\3\2\2\2")
        buf.write(u"\u01c8\u01c9\7\63\2\2\u01c9g\3\2\2\2\u01ca\u01cb\7\62")
        buf.write(u"\2\2\u01cbi\3\2\2\2\u01cc\u01cd\t\2\2\2\u01cdk\3\2\2")
        buf.write(u"\2\u01ce\u01cf\t\3\2\2\u01cfm\3\2\2\2\u01d0\u01d1\t\4")
        buf.write(u"\2\2\u01d1o\3\2\2\2\u01d2\u01d3\t\5\2\2\u01d3q\3\2\2")
        buf.write(u"\2\u01d4\u01d5\t\6\2\2\u01d5s\3\2\2\2\u01d6\u01d7\t\7")
        buf.write(u"\2\2\u01d7u\3\2\2\2\u01d8\u01d9\t\b\2\2\u01d9w\3\2\2")
        buf.write(u"\2\u01da\u01db\7\61\2\2\u01dby\3\2\2\2%}\177\u008a\u0096")
        buf.write(u"\u009e\u00a4\u00a8\u00b1\u00c1\u00c5\u00ca\u00d3\u00de")
        buf.write(u"\u00e7\u00f0\u00f5\u010a\u0111\u0120\u0124\u0131\u0135")
        buf.write(u"\u0139\u0140\u0144\u0153\u0158\u016c\u0177\u0180\u0191")
        buf.write(u"\u01a7\u01a9\u01b6\u01c4")
        return buf.getvalue()
		

class LLangParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'Bool'", u"'Int'", u"'Str'", u"'None'", 
                     u"'record'", u"'writeln'", u"'readln'", u"'else'", 
                     u"'for'", u"'while'", u"'if'", u"'elif'", u"'return'", 
                     u"'fun'", u"'pass'", u"'('", u"')'", u"'{'", u"'}'", 
                     u"'['", u"']'", u"';'", u"','", u"'.'", u"'='", u"'>'", 
                     u"'<'", u"'!'", u"':'", u"'=='", u"'<='", u"'>='", 
                     u"'!='", u"'&&'", u"'||'", u"'+'", u"'-'", u"'*'", 
                     u"'/'", u"'%'", u"'+='", u"'-='", u"'*='", u"'/='", 
                     u"'&='", u"'%='" ]

    symbolicNames = [ u"<INVALID>", u"BOOL", u"INT", u"STR", u"NONE", u"RECORD", 
                      u"WRITELN", u"READLN", u"ELSE", u"FOR", u"WHILE", 
                      u"IF", u"ELIF", u"RETURN", u"FUN", u"PASS", u"LPAREN", 
                      u"RPAREN", u"LBRACE", u"RBRACE", u"LBRACK", u"RBRACK", 
                      u"SEMI", u"COMMA", u"DOT", u"ASSIGN", u"GT", u"LT", 
                      u"BANG", u"COLON", u"EQUAL", u"LE", u"GE", u"NOTEQUAL", 
                      u"AND", u"OR", u"ADD", u"SUB", u"MUL", u"DIV", u"MOD", 
                      u"ADD_ASSIGN", u"SUB_ASSIGN", u"MUL_ASSIGN", u"DIV_ASSIGN", 
                      u"AND_ASSIGN", u"MOD_ASSIGN", u"Identifier", u"BooleanLiteral", 
                      u"StringLiteral", u"IntegerLiteral", u"WS", u"COMMENT", 
                      u"LINE_COMMENT" ]

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
    RULE_variableInitializer = 11
    RULE_recordInitializer = 12
    RULE_recordFieldInitializerList = 13
    RULE_recordFieldInitializer = 14
    RULE_cortegeInitializer = 15
    RULE_variableInitializerNonEmptyList = 16
    RULE_passStatement = 17
    RULE_exprType = 18
    RULE_primitiveType = 19
    RULE_recordType = 20
    RULE_intType = 21
    RULE_strType = 22
    RULE_boolType = 23
    RULE_voidType = 24
    RULE_cortegeType = 25
    RULE_typeNonEmptyList = 26
    RULE_block = 27
    RULE_statement = 28
    RULE_returnStatement = 29
    RULE_whileStatement = 30
    RULE_forStatement = 31
    RULE_forInit = 32
    RULE_forUpdate = 33
    RULE_ifStatement = 34
    RULE_writelnStatement = 35
    RULE_writelnCall = 36
    RULE_readlnStatement = 37
    RULE_readlnCall = 38
    RULE_functionInvocationStatement = 39
    RULE_functionInvocation = 40
    RULE_argumentList = 41
    RULE_expression = 42
    RULE_assignmentStatement = 43
    RULE_assignment = 44
    RULE_leftHandSide = 45
    RULE_cortegeAccess = 46
    RULE_recordFieldAccess = 47
    RULE_literal = 48
    RULE_intLiteral = 49
    RULE_strLiteral = 50
    RULE_boolLiteral = 51
    RULE_unaryOperator = 52
    RULE_mulDivModOperator = 53
    RULE_addSubOperator = 54
    RULE_compareOperator = 55
    RULE_equalOrNotOperator = 56
    RULE_boolOperator = 57
    RULE_assignmentOperator = 58
    RULE_identifier = 59

    ruleNames =  [ u"programme", u"recordDeclaration", u"recordBody", u"functionDeclaration", 
                   u"functionSignature", u"functionReturnType", u"functionBody", 
                   u"functionParameterList", u"functionParameter", u"variableDeclarationStatement", 
                   u"variableDeclaration", u"variableInitializer", u"recordInitializer", 
                   u"recordFieldInitializerList", u"recordFieldInitializer", 
                   u"cortegeInitializer", u"variableInitializerNonEmptyList", 
                   u"passStatement", u"exprType", u"primitiveType", u"recordType", 
                   u"intType", u"strType", u"boolType", u"voidType", u"cortegeType", 
                   u"typeNonEmptyList", u"block", u"statement", u"returnStatement", 
                   u"whileStatement", u"forStatement", u"forInit", u"forUpdate", 
                   u"ifStatement", u"writelnStatement", u"writelnCall", 
                   u"readlnStatement", u"readlnCall", u"functionInvocationStatement", 
                   u"functionInvocation", u"argumentList", u"expression", 
                   u"assignmentStatement", u"assignment", u"leftHandSide", 
                   u"cortegeAccess", u"recordFieldAccess", u"literal", u"intLiteral", 
                   u"strLiteral", u"boolLiteral", u"unaryOperator", u"mulDivModOperator", 
                   u"addSubOperator", u"compareOperator", u"equalOrNotOperator", 
                   u"boolOperator", u"assignmentOperator", u"identifier" ]

    EOF = Token.EOF
    BOOL=1
    INT=2
    STR=3
    NONE=4
    RECORD=5
    WRITELN=6
    READLN=7
    ELSE=8
    FOR=9
    WHILE=10
    IF=11
    ELIF=12
    RETURN=13
    FUN=14
    PASS=15
    LPAREN=16
    RPAREN=17
    LBRACE=18
    RBRACE=19
    LBRACK=20
    RBRACK=21
    SEMI=22
    COMMA=23
    DOT=24
    ASSIGN=25
    GT=26
    LT=27
    BANG=28
    COLON=29
    EQUAL=30
    LE=31
    GE=32
    NOTEQUAL=33
    AND=34
    OR=35
    ADD=36
    SUB=37
    MUL=38
    DIV=39
    MOD=40
    ADD_ASSIGN=41
    SUB_ASSIGN=42
    MUL_ASSIGN=43
    DIV_ASSIGN=44
    AND_ASSIGN=45
    MOD_ASSIGN=46
    Identifier=47
    BooleanLiteral=48
    StringLiteral=49
    IntegerLiteral=50
    WS=51
    COMMENT=52
    LINE_COMMENT=53

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
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.RECORD) | (1 << LLangParser.FUN) | (1 << LLangParser.LBRACK) | (1 << LLangParser.Identifier))) != 0):
                self.state = 123
                token = self._input.LA(1)
                if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.LBRACK, LLangParser.Identifier]:
                    self.state = 120 
                    self.variableDeclarationStatement()

                elif token in [LLangParser.FUN]:
                    self.state = 121 
                    self.functionDeclaration()

                elif token in [LLangParser.RECORD]:
                    self.state = 122 
                    self.recordDeclaration()

                else:
                    raise NoViableAltException(self)

                self.state = 127
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

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


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
            self.state = 128
            self.match(LLangParser.RECORD)
            self.state = 129 
            self.identifier()
            self.state = 130 
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
            self.state = 132
            self.match(LLangParser.LBRACE)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.LBRACK) | (1 << LLangParser.Identifier))) != 0):
                self.state = 133 
                self.variableDeclarationStatement()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(LLangParser.RBRACE)
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
            self.state = 141
            self.match(LLangParser.FUN)
            self.state = 142 
            self.functionSignature()
            self.state = 143 
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
            self.state = 145 
            self.identifier()
            self.state = 146
            self.match(LLangParser.LPAREN)
            self.state = 148
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 147 
                self.functionParameterList()


            self.state = 150
            self.match(LLangParser.RPAREN)
            self.state = 151
            self.match(LLangParser.COLON)
            self.state = 152 
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
            self.state = 156
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.LBRACK, LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154 
                self.exprType()

            elif token in [LLangParser.NONE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155 
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


        def returnStatement(self):
            return self.getTypedRuleContext(LLangParser.ReturnStatementContext,0)


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
            self.state = 158
            self.match(LLangParser.LBRACE)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.LBRACE) | (1 << LLangParser.LBRACK) | (1 << LLangParser.Identifier))) != 0):
                self.state = 159 
                self.statement()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            _la = self._input.LA(1)
            if _la==LLangParser.RETURN:
                self.state = 165 
                self.returnStatement()


            self.state = 168
            self.match(LLangParser.RBRACE)
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


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.COMMA)
            else:
                return self.getToken(LLangParser.COMMA, i)

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
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 170 
                    self.functionParameter()
                    self.state = 171
                    self.match(LLangParser.COMMA) 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 178 
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
            self.state = 180 
            self.identifier()
            self.state = 181
            self.match(LLangParser.COLON)
            self.state = 182 
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
            self.state = 184 
            self.variableDeclaration()
            self.state = 185
            self.match(LLangParser.SEMI)
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


        def variableInitializer(self):
            return self.getTypedRuleContext(LLangParser.VariableInitializerContext,0)


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
            self.state = 187 
            self.exprType()
            self.state = 188 
            self.identifier()
            self.state = 191
            _la = self._input.LA(1)
            if _la==LLangParser.ASSIGN:
                self.state = 189
                self.match(LLangParser.ASSIGN)
                self.state = 190 
                self.variableInitializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def cortegeInitializer(self):
            return self.getTypedRuleContext(LLangParser.CortegeInitializerContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_variableInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableInitializer(self)
            else:
                return visitor.visitChildren(self)




    def variableInitializer(self):

        localctx = LLangParser.VariableInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variableInitializer)
        try:
            self.state = 195
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193 
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194 
                self.cortegeInitializer()
                pass


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
        self.enterRule(localctx, 24, self.RULE_recordInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197 
            self.identifier()
            self.state = 198
            self.match(LLangParser.LPAREN)
            self.state = 200
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 199 
                self.recordFieldInitializerList()


            self.state = 202
            self.match(LLangParser.RPAREN)
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


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.COMMA)
            else:
                return self.getToken(LLangParser.COMMA, i)

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
        self.enterRule(localctx, 26, self.RULE_recordFieldInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 204 
                    self.recordFieldInitializer()
                    self.state = 205
                    self.match(LLangParser.COMMA) 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 212 
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
        self.enterRule(localctx, 28, self.RULE_recordFieldInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214 
            self.identifier()
            self.state = 215
            self.match(LLangParser.ASSIGN)
            self.state = 216 
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

        def variableInitializerNonEmptyList(self):
            return self.getTypedRuleContext(LLangParser.VariableInitializerNonEmptyListContext,0)


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
        self.enterRule(localctx, 30, self.RULE_cortegeInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(LLangParser.LBRACK)
            self.state = 220
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.LPAREN) | (1 << LLangParser.LBRACK) | (1 << LLangParser.BANG) | (1 << LLangParser.SUB) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 219 
                self.variableInitializerNonEmptyList()


            self.state = 222
            self.match(LLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableInitializerNonEmptyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableInitializerNonEmptyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableInitializer(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.VariableInitializerContext)
            else:
                return self.getTypedRuleContext(LLangParser.VariableInitializerContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.COMMA)
            else:
                return self.getToken(LLangParser.COMMA, i)

        def getRuleIndex(self):
            return LLangParser.RULE_variableInitializerNonEmptyList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableInitializerNonEmptyList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableInitializerNonEmptyList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableInitializerNonEmptyList(self)
            else:
                return visitor.visitChildren(self)




    def variableInitializerNonEmptyList(self):

        localctx = LLangParser.VariableInitializerNonEmptyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variableInitializerNonEmptyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224 
            self.variableInitializer()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.COMMA:
                self.state = 225
                self.match(LLangParser.COMMA)
                self.state = 226 
                self.variableInitializer()
                self.state = 231
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
        self.enterRule(localctx, 34, self.RULE_passStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(LLangParser.PASS)
            self.state = 233
            self.match(LLangParser.SEMI)
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


        def recordType(self):
            return self.getTypedRuleContext(LLangParser.RecordTypeContext,0)


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
        self.enterRule(localctx, 36, self.RULE_exprType)
        try:
            self.state = 238
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235 
                self.primitiveType()

            elif token in [LLangParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236 
                self.cortegeType()

            elif token in [LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 237 
                self.recordType()

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
        self.enterRule(localctx, 38, self.RULE_primitiveType)
        try:
            self.state = 243
            token = self._input.LA(1)
            if token in [LLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240 
                self.intType()

            elif token in [LLangParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241 
                self.strType()

            elif token in [LLangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242 
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

    class RecordTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(LLangParser.Identifier, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_recordType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordType(self)
            else:
                return visitor.visitChildren(self)




    def recordType(self):

        localctx = LLangParser.RecordTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_recordType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
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
        self.enterRule(localctx, 42, self.RULE_intType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
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
        self.enterRule(localctx, 44, self.RULE_strType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
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
        self.enterRule(localctx, 46, self.RULE_boolType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
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
        self.enterRule(localctx, 48, self.RULE_voidType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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

        def typeNonEmptyList(self):
            return self.getTypedRuleContext(LLangParser.TypeNonEmptyListContext,0)


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
        self.enterRule(localctx, 50, self.RULE_cortegeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(LLangParser.LBRACK)
            self.state = 256 
            self.typeNonEmptyList()
            self.state = 257
            self.match(LLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeNonEmptyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.TypeNonEmptyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exprType(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExprTypeContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExprTypeContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.COMMA)
            else:
                return self.getToken(LLangParser.COMMA, i)

        def getRuleIndex(self):
            return LLangParser.RULE_typeNonEmptyList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterTypeNonEmptyList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitTypeNonEmptyList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitTypeNonEmptyList(self)
            else:
                return visitor.visitChildren(self)




    def typeNonEmptyList(self):

        localctx = LLangParser.TypeNonEmptyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typeNonEmptyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259 
            self.exprType()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.COMMA:
                self.state = 260
                self.match(LLangParser.COMMA)
                self.state = 261 
                self.exprType()
                self.state = 266
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
            self.state = 267
            self.match(LLangParser.LBRACE)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.LBRACE) | (1 << LLangParser.LBRACK) | (1 << LLangParser.Identifier))) != 0):
                self.state = 268 
                self.statement()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 274
            self.match(LLangParser.RBRACE)
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

        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


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
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 286
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276 
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277 
                self.variableDeclarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278 
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 279 
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 280 
                self.functionInvocationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 281 
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 282 
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 283 
                self.passStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 284 
                self.readlnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 285 
                self.writelnStatement()
                pass


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

        def RETURN(self):
            return self.getToken(LLangParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


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
        self.enterRule(localctx, 58, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(LLangParser.RETURN)
            self.state = 290
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.LPAREN) | (1 << LLangParser.LBRACK) | (1 << LLangParser.BANG) | (1 << LLangParser.SUB) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 289 
                self.expression(0)


            self.state = 292
            self.match(LLangParser.SEMI)
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
        self.enterRule(localctx, 60, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(LLangParser.WHILE)
            self.state = 295
            self.match(LLangParser.LPAREN)
            self.state = 296 
            self.expression(0)
            self.state = 297
            self.match(LLangParser.RPAREN)
            self.state = 298 
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

        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(LLangParser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(LLangParser.ForUpdateContext,0)


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
        self.enterRule(localctx, 62, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(LLangParser.FOR)
            self.state = 301
            self.match(LLangParser.LPAREN)
            self.state = 303
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.LBRACK) | (1 << LLangParser.Identifier))) != 0):
                self.state = 302 
                self.forInit()


            self.state = 305
            self.match(LLangParser.SEMI)
            self.state = 307
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.LPAREN) | (1 << LLangParser.LBRACK) | (1 << LLangParser.BANG) | (1 << LLangParser.SUB) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 306 
                self.expression(0)


            self.state = 309
            self.match(LLangParser.SEMI)
            self.state = 311
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 310 
                self.forUpdate()


            self.state = 313
            self.match(LLangParser.RPAREN)
            self.state = 314 
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
        self.enterRule(localctx, 64, self.RULE_forInit)
        try:
            self.state = 318
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317 
                self.variableDeclaration()
                pass


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
        self.enterRule(localctx, 66, self.RULE_forUpdate)
        try:
            self.state = 322
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321 
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

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def block(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(LLangParser.BlockContext,i)


        def ELIF(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.ELIF)
            else:
                return self.getToken(LLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(LLangParser.ELSE, 0)

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
        self.enterRule(localctx, 68, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(LLangParser.IF)
            self.state = 325
            self.match(LLangParser.LPAREN)
            self.state = 326 
            self.expression(0)
            self.state = 327
            self.match(LLangParser.RPAREN)
            self.state = 328 
            self.block()
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.ELIF:
                self.state = 329
                self.match(LLangParser.ELIF)
                self.state = 330
                self.match(LLangParser.LPAREN)
                self.state = 331 
                self.expression(0)
                self.state = 332
                self.match(LLangParser.RPAREN)
                self.state = 333 
                self.block()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 342
            _la = self._input.LA(1)
            if _la==LLangParser.ELSE:
                self.state = 340
                self.match(LLangParser.ELSE)
                self.state = 341 
                self.block()


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
        self.enterRule(localctx, 70, self.RULE_writelnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344 
            self.writelnCall()
            self.state = 345
            self.match(LLangParser.SEMI)
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
        self.enterRule(localctx, 72, self.RULE_writelnCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(LLangParser.WRITELN)
            self.state = 348
            self.match(LLangParser.LPAREN)
            self.state = 349 
            self.argumentList()
            self.state = 350
            self.match(LLangParser.RPAREN)
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

        def readlnCall(self):
            return self.getTypedRuleContext(LLangParser.ReadlnCallContext,0)


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
        self.enterRule(localctx, 74, self.RULE_readlnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352 
            self.readlnCall()
            self.state = 353
            self.match(LLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadlnCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReadlnCallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def READLN(self):
            return self.getToken(LLangParser.READLN, 0)

        def leftHandSide(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.LeftHandSideContext)
            else:
                return self.getTypedRuleContext(LLangParser.LeftHandSideContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.COMMA)
            else:
                return self.getToken(LLangParser.COMMA, i)

        def getRuleIndex(self):
            return LLangParser.RULE_readlnCall

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReadlnCall(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReadlnCall(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReadlnCall(self)
            else:
                return visitor.visitChildren(self)




    def readlnCall(self):

        localctx = LLangParser.ReadlnCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_readlnCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(LLangParser.READLN)
            self.state = 356
            self.match(LLangParser.LPAREN)
            self.state = 357 
            self.leftHandSide()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.COMMA:
                self.state = 358
                self.match(LLangParser.COMMA)
                self.state = 359 
                self.leftHandSide()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
            self.match(LLangParser.RPAREN)
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
        self.enterRule(localctx, 78, self.RULE_functionInvocationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367 
            self.functionInvocation()
            self.state = 368
            self.match(LLangParser.SEMI)
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
        self.enterRule(localctx, 80, self.RULE_functionInvocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370 
            self.identifier()
            self.state = 371
            self.match(LLangParser.LPAREN)
            self.state = 373
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.LPAREN) | (1 << LLangParser.LBRACK) | (1 << LLangParser.BANG) | (1 << LLangParser.SUB) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 372 
                self.argumentList()


            self.state = 375
            self.match(LLangParser.RPAREN)
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


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.COMMA)
            else:
                return self.getToken(LLangParser.COMMA, i)

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
        self.enterRule(localctx, 82, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377 
            self.expression(0)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.COMMA:
                self.state = 378
                self.match(LLangParser.COMMA)
                self.state = 379 
                self.expression(0)
                self.state = 384
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


        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 386 
                self.unaryOperator()
                self.state = 387 
                self.expression(12)
                pass

            elif la_ == 2:
                self.state = 389 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 390 
                self.functionInvocation()
                pass

            elif la_ == 4:
                self.state = 391 
                self.literal()
                pass

            elif la_ == 5:
                self.state = 392 
                self.cortegeInitializer()
                pass

            elif la_ == 6:
                self.state = 393 
                self.recordInitializer()
                pass

            elif la_ == 7:
                self.state = 394 
                self.leftHandSide()
                pass

            elif la_ == 8:
                self.state = 395
                self.match(LLangParser.LPAREN)
                self.state = 396 
                self.expression(0)
                self.state = 397
                self.match(LLangParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 421
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 401
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 402 
                        self.mulDivModOperator()
                        self.state = 403 
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 405
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 406 
                        self.addSubOperator()
                        self.state = 407 
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 409
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 410 
                        self.compareOperator()
                        self.state = 411 
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 413
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 414 
                        self.equalOrNotOperator()
                        self.state = 415 
                        self.expression(9)
                        pass

                    elif la_ == 5:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 417
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 418 
                        self.boolOperator()
                        self.state = 419 
                        self.expression(8)
                        pass

             
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426 
            self.assignment()
            self.state = 427
            self.match(LLangParser.SEMI)
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
        self.enterRule(localctx, 88, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429 
            self.leftHandSide()
            self.state = 430 
            self.assignmentOperator()
            self.state = 431 
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


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


        def recordFieldAccess(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldAccessContext,0)


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
        self.enterRule(localctx, 90, self.RULE_leftHandSide)
        try:
            self.state = 436
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433 
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434 
                self.cortegeAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 435 
                self.recordFieldAccess()
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


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


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




    def cortegeAccess(self):

        localctx = LLangParser.CortegeAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_cortegeAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438 
            self.identifier()
            self.state = 439
            self.match(LLangParser.LBRACK)
            self.state = 440 
            self.expression(0)
            self.state = 441
            self.match(LLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordFieldAccessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldAccessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def leftHandSide(self):
            return self.getTypedRuleContext(LLangParser.LeftHandSideContext,0)


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




    def recordFieldAccess(self):

        localctx = LLangParser.RecordFieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_recordFieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443 
            self.identifier()
            self.state = 444
            self.match(LLangParser.DOT)
            self.state = 445 
            self.leftHandSide()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 96, self.RULE_literal)
        try:
            self.state = 450
            token = self._input.LA(1)
            if token in [LLangParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447 
                self.intLiteral()

            elif token in [LLangParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448 
                self.strLiteral()

            elif token in [LLangParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449 
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
        self.enterRule(localctx, 98, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
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
        self.enterRule(localctx, 100, self.RULE_strLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
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
        self.enterRule(localctx, 102, self.RULE_boolLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
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
        self.enterRule(localctx, 104, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            _la = self._input.LA(1)
            if not(_la==LLangParser.BANG or _la==LLangParser.SUB):
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
        self.enterRule(localctx, 106, self.RULE_mulDivModOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.MUL) | (1 << LLangParser.DIV) | (1 << LLangParser.MOD))) != 0)):
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
        self.enterRule(localctx, 108, self.RULE_addSubOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            _la = self._input.LA(1)
            if not(_la==LLangParser.ADD or _la==LLangParser.SUB):
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
        self.enterRule(localctx, 110, self.RULE_compareOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.GT) | (1 << LLangParser.LT) | (1 << LLangParser.LE) | (1 << LLangParser.GE))) != 0)):
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
        self.enterRule(localctx, 112, self.RULE_equalOrNotOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            _la = self._input.LA(1)
            if not(_la==LLangParser.EQUAL or _la==LLangParser.NOTEQUAL):
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
        self.enterRule(localctx, 114, self.RULE_boolOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            _la = self._input.LA(1)
            if not(_la==LLangParser.AND or _la==LLangParser.OR):
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
        self.enterRule(localctx, 116, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.ASSIGN) | (1 << LLangParser.ADD_ASSIGN) | (1 << LLangParser.SUB_ASSIGN) | (1 << LLangParser.MUL_ASSIGN) | (1 << LLangParser.DIV_ASSIGN) | (1 << LLangParser.MOD_ASSIGN))) != 0)):
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
        self.enterRule(localctx, 118, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
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
        self._predicates[42] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         



