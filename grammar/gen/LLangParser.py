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
        buf.write(u"\67\u01ff\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\3\2\3\2\3\2\3\2\7\2\u0089\n\2\f\2\16\2\u008c\13")
        buf.write(u"\2\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u0094\n\4\f\4\16\4\u0097")
        buf.write(u"\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u00a2\n")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7\u00aa\n\7\3\b\3\b\7\b")
        buf.write(u"\u00ae\n\b\f\b\16\b\u00b1\13\b\3\b\5\b\u00b4\n\b\3\b")
        buf.write(u"\3\b\3\t\3\t\3\t\7\t\u00bb\n\t\f\t\16\t\u00be\13\t\3")
        buf.write(u"\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write(u"\5\f\u00cd\n\f\3\r\3\r\3\r\3\r\5\r\u00d3\n\r\3\r\3\r")
        buf.write(u"\3\16\3\16\3\16\7\16\u00da\n\16\f\16\16\16\u00dd\13\16")
        buf.write(u"\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00e7\n")
        buf.write(u"\20\3\20\3\20\3\21\3\21\3\21\7\21\u00ee\n\21\f\21\16")
        buf.write(u"\21\u00f1\13\21\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00f9")
        buf.write(u"\n\23\3\24\3\24\3\24\5\24\u00fe\n\24\3\25\3\25\3\26\3")
        buf.write(u"\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write(u"\3\33\3\33\5\33\u0110\n\33\3\34\3\34\3\34\7\34\u0115")
        buf.write(u"\n\34\f\34\16\34\u0118\13\34\3\35\3\35\7\35\u011c\n\35")
        buf.write(u"\f\35\16\35\u011f\13\35\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u012f\n")
        buf.write(u"\37\3 \3 \3 \3!\3!\5!\u0136\n!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write(u"\"\3#\3#\3#\5#\u0141\n#\3#\3#\5#\u0145\n#\3#\3#\5#\u0149")
        buf.write(u"\n#\3#\3#\3#\3$\3$\5$\u0150\n$\3%\3%\3&\3&\5&\u0156\n")
        buf.write(u"&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u015e\n\'\f\'\16\'\u0161")
        buf.write(u"\13\'\3\'\5\'\u0164\n\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(u"*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\7-\u017f")
        buf.write(u"\n-\f-\16-\u0182\13-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write(u"\60\3\60\3\60\7\60\u0191\n\60\f\60\16\60\u0194\13\60")
        buf.write(u"\5\60\u0196\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\5\61\u01a5\n\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u01bb\n\61")
        buf.write(u"\f\61\16\61\u01be\13\61\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write(u"\3\63\3\64\3\64\3\64\5\64\u01ca\n\64\3\65\3\65\3\65\3")
        buf.write(u"\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u01d7\n\65")
        buf.write(u"\f\65\16\65\u01da\13\65\3\66\3\66\3\66\5\66\u01df\n\66")
        buf.write(u"\3\66\5\66\u01e2\n\66\3\67\3\67\3\67\5\67\u01e7\n\67")
        buf.write(u"\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3")
        buf.write(u"@\3A\3A\3B\3B\3B\2\4`hC\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write(u"\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`")
        buf.write(u"bdfhjlnprtvxz|~\u0080\u0082\2\t\3\2\17\20\3\2\21\23\4")
        buf.write(u"\2\17\17\24\24\3\2\25\30\3\2\31\32\3\2\33\34\4\2\n\n")
        buf.write(u"\35!\u01f9\2\u008a\3\2\2\2\4\u008d\3\2\2\2\6\u0091\3")
        buf.write(u"\2\2\2\b\u009a\3\2\2\2\n\u009e\3\2\2\2\f\u00a9\3\2\2")
        buf.write(u"\2\16\u00ab\3\2\2\2\20\u00bc\3\2\2\2\22\u00c1\3\2\2\2")
        buf.write(u"\24\u00c5\3\2\2\2\26\u00c8\3\2\2\2\30\u00ce\3\2\2\2\32")
        buf.write(u"\u00db\3\2\2\2\34\u00e0\3\2\2\2\36\u00e4\3\2\2\2 \u00ea")
        buf.write(u"\3\2\2\2\"\u00f2\3\2\2\2$\u00f8\3\2\2\2&\u00fd\3\2\2")
        buf.write(u"\2(\u00ff\3\2\2\2*\u0101\3\2\2\2,\u0103\3\2\2\2.\u0105")
        buf.write(u"\3\2\2\2\60\u0107\3\2\2\2\62\u0109\3\2\2\2\64\u010f\3")
        buf.write(u"\2\2\2\66\u0111\3\2\2\28\u0119\3\2\2\2:\u0122\3\2\2\2")
        buf.write(u"<\u012e\3\2\2\2>\u0130\3\2\2\2@\u0133\3\2\2\2B\u0137")
        buf.write(u"\3\2\2\2D\u013d\3\2\2\2F\u014f\3\2\2\2H\u0151\3\2\2\2")
        buf.write(u"J\u0155\3\2\2\2L\u0157\3\2\2\2N\u0165\3\2\2\2P\u016b")
        buf.write(u"\3\2\2\2R\u016e\3\2\2\2T\u0171\3\2\2\2V\u0176\3\2\2\2")
        buf.write(u"X\u0179\3\2\2\2Z\u0185\3\2\2\2\\\u0188\3\2\2\2^\u0195")
        buf.write(u"\3\2\2\2`\u01a4\3\2\2\2b\u01bf\3\2\2\2d\u01c2\3\2\2\2")
        buf.write(u"f\u01c9\3\2\2\2h\u01cb\3\2\2\2j\u01e1\3\2\2\2l\u01e6")
        buf.write(u"\3\2\2\2n\u01e8\3\2\2\2p\u01ea\3\2\2\2r\u01ec\3\2\2\2")
        buf.write(u"t\u01ee\3\2\2\2v\u01f0\3\2\2\2x\u01f2\3\2\2\2z\u01f4")
        buf.write(u"\3\2\2\2|\u01f6\3\2\2\2~\u01f8\3\2\2\2\u0080\u01fa\3")
        buf.write(u"\2\2\2\u0082\u01fc\3\2\2\2\u0084\u0089\5\24\13\2\u0085")
        buf.write(u"\u0089\5\b\5\2\u0086\u0089\5\4\3\2\u0087\u0089\5:\36")
        buf.write(u"\2\u0088\u0084\3\2\2\2\u0088\u0085\3\2\2\2\u0088\u0086")
        buf.write(u"\3\2\2\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a")
        buf.write(u"\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\3\3\2\2\2\u008c")
        buf.write(u"\u008a\3\2\2\2\u008d\u008e\7&\2\2\u008e\u008f\5(\25\2")
        buf.write(u"\u008f\u0090\5\6\4\2\u0090\5\3\2\2\2\u0091\u0095\7\3")
        buf.write(u"\2\2\u0092\u0094\5\24\13\2\u0093\u0092\3\2\2\2\u0094")
        buf.write(u"\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2")
        buf.write(u"\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099")
        buf.write(u"\7\4\2\2\u0099\7\3\2\2\2\u009a\u009b\7/\2\2\u009b\u009c")
        buf.write(u"\5\n\6\2\u009c\u009d\5\16\b\2\u009d\t\3\2\2\2\u009e\u009f")
        buf.write(u"\5\u0082B\2\u009f\u00a1\7\5\2\2\u00a0\u00a2\5\20\t\2")
        buf.write(u"\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write(u"\3\2\2\2\u00a3\u00a4\7\6\2\2\u00a4\u00a5\7\7\2\2\u00a5")
        buf.write(u"\u00a6\5\f\7\2\u00a6\13\3\2\2\2\u00a7\u00aa\5$\23\2\u00a8")
        buf.write(u"\u00aa\5\60\31\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2")
        buf.write(u"\2\2\u00aa\r\3\2\2\2\u00ab\u00af\7\3\2\2\u00ac\u00ae")
        buf.write(u"\5<\37\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af")
        buf.write(u"\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b3\3\2\2")
        buf.write(u"\2\u00b1\u00af\3\2\2\2\u00b2\u00b4\5> \2\u00b3\u00b2")
        buf.write(u"\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write(u"\u00b6\7\4\2\2\u00b6\17\3\2\2\2\u00b7\u00b8\5\22\n\2")
        buf.write(u"\u00b8\u00b9\7\b\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b7")
        buf.write(u"\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc")
        buf.write(u"\u00bd\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bc\3\2\2")
        buf.write(u"\2\u00bf\u00c0\5\22\n\2\u00c0\21\3\2\2\2\u00c1\u00c2")
        buf.write(u"\5\u0082B\2\u00c2\u00c3\7\7\2\2\u00c3\u00c4\5$\23\2\u00c4")
        buf.write(u"\23\3\2\2\2\u00c5\u00c6\5\26\f\2\u00c6\u00c7\7\t\2\2")
        buf.write(u"\u00c7\25\3\2\2\2\u00c8\u00c9\5$\23\2\u00c9\u00cc\5\u0082")
        buf.write(u"B\2\u00ca\u00cb\7\n\2\2\u00cb\u00cd\5`\61\2\u00cc\u00ca")
        buf.write(u"\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\27\3\2\2\2\u00ce\u00cf")
        buf.write(u"\7\13\2\2\u00cf\u00d0\5\u0082B\2\u00d0\u00d2\7\5\2\2")
        buf.write(u"\u00d1\u00d3\5\32\16\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3")
        buf.write(u"\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7\6\2\2\u00d5")
        buf.write(u"\31\3\2\2\2\u00d6\u00d7\5\34\17\2\u00d7\u00d8\7\b\2\2")
        buf.write(u"\u00d8\u00da\3\2\2\2\u00d9\u00d6\3\2\2\2\u00da\u00dd")
        buf.write(u"\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write(u"\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\5\34\17")
        buf.write(u"\2\u00df\33\3\2\2\2\u00e0\u00e1\5\u0082B\2\u00e1\u00e2")
        buf.write(u"\7\n\2\2\u00e2\u00e3\5`\61\2\u00e3\35\3\2\2\2\u00e4\u00e6")
        buf.write(u"\7\f\2\2\u00e5\u00e7\5 \21\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write(u"\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\7\r\2")
        buf.write(u"\2\u00e9\37\3\2\2\2\u00ea\u00ef\5`\61\2\u00eb\u00ec\7")
        buf.write(u"\b\2\2\u00ec\u00ee\5`\61\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write(u"\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2")
        buf.write(u"\2\u00f0!\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7\60")
        buf.write(u"\2\2\u00f3\u00f4\7\t\2\2\u00f4#\3\2\2\2\u00f5\u00f9\5")
        buf.write(u"&\24\2\u00f6\u00f9\5\62\32\2\u00f7\u00f9\5(\25\2\u00f8")
        buf.write(u"\u00f5\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2")
        buf.write(u"\2\u00f9%\3\2\2\2\u00fa\u00fe\5*\26\2\u00fb\u00fe\5,")
        buf.write(u"\27\2\u00fc\u00fe\5.\30\2\u00fd\u00fa\3\2\2\2\u00fd\u00fb")
        buf.write(u"\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\'\3\2\2\2\u00ff\u0100")
        buf.write(u"\7\61\2\2\u0100)\3\2\2\2\u0101\u0102\7#\2\2\u0102+\3")
        buf.write(u"\2\2\2\u0103\u0104\7$\2\2\u0104-\3\2\2\2\u0105\u0106")
        buf.write(u"\7\"\2\2\u0106/\3\2\2\2\u0107\u0108\7%\2\2\u0108\61\3")
        buf.write(u"\2\2\2\u0109\u010a\7\f\2\2\u010a\u010b\5\66\34\2\u010b")
        buf.write(u"\u010c\7\r\2\2\u010c\63\3\2\2\2\u010d\u0110\5&\24\2\u010e")
        buf.write(u"\u0110\5\62\32\2\u010f\u010d\3\2\2\2\u010f\u010e\3\2")
        buf.write(u"\2\2\u0110\65\3\2\2\2\u0111\u0116\5\64\33\2\u0112\u0113")
        buf.write(u"\7\b\2\2\u0113\u0115\5\64\33\2\u0114\u0112\3\2\2\2\u0115")
        buf.write(u"\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2")
        buf.write(u"\2\u0117\67\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011d\7")
        buf.write(u"\3\2\2\u011a\u011c\5<\37\2\u011b\u011a\3\2\2\2\u011c")
        buf.write(u"\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2")
        buf.write(u"\2\u011e\u0120\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121")
        buf.write(u"\7\4\2\2\u01219\3\2\2\2\u0122\u0123\58\35\2\u0123;\3")
        buf.write(u"\2\2\2\u0124\u012f\5:\36\2\u0125\u012f\5\24\13\2\u0126")
        buf.write(u"\u012f\5b\62\2\u0127\u012f\5L\'\2\u0128\u012f\5Z.\2\u0129")
        buf.write(u"\u012f\5D#\2\u012a\u012f\5B\"\2\u012b\u012f\5\"\22\2")
        buf.write(u"\u012c\u012f\5V,\2\u012d\u012f\5R*\2\u012e\u0124\3\2")
        buf.write(u"\2\2\u012e\u0125\3\2\2\2\u012e\u0126\3\2\2\2\u012e\u0127")
        buf.write(u"\3\2\2\2\u012e\u0128\3\2\2\2\u012e\u0129\3\2\2\2\u012e")
        buf.write(u"\u012a\3\2\2\2\u012e\u012b\3\2\2\2\u012e\u012c\3\2\2")
        buf.write(u"\2\u012e\u012d\3\2\2\2\u012f=\3\2\2\2\u0130\u0131\5@")
        buf.write(u"!\2\u0131\u0132\7\t\2\2\u0132?\3\2\2\2\u0133\u0135\7")
        buf.write(u".\2\2\u0134\u0136\5`\61\2\u0135\u0134\3\2\2\2\u0135\u0136")
        buf.write(u"\3\2\2\2\u0136A\3\2\2\2\u0137\u0138\7+\2\2\u0138\u0139")
        buf.write(u"\7\5\2\2\u0139\u013a\5`\61\2\u013a\u013b\7\6\2\2\u013b")
        buf.write(u"\u013c\58\35\2\u013cC\3\2\2\2\u013d\u013e\7*\2\2\u013e")
        buf.write(u"\u0140\7\5\2\2\u013f\u0141\5F$\2\u0140\u013f\3\2\2\2")
        buf.write(u"\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144")
        buf.write(u"\7\t\2\2\u0143\u0145\5H%\2\u0144\u0143\3\2\2\2\u0144")
        buf.write(u"\u0145\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\7\t\2")
        buf.write(u"\2\u0147\u0149\5J&\2\u0148\u0147\3\2\2\2\u0148\u0149")
        buf.write(u"\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\7\6\2\2\u014b")
        buf.write(u"\u014c\58\35\2\u014cE\3\2\2\2\u014d\u0150\5d\63\2\u014e")
        buf.write(u"\u0150\5\26\f\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2")
        buf.write(u"\2\u0150G\3\2\2\2\u0151\u0152\5`\61\2\u0152I\3\2\2\2")
        buf.write(u"\u0153\u0156\5d\63\2\u0154\u0156\5\\/\2\u0155\u0153\3")
        buf.write(u"\2\2\2\u0155\u0154\3\2\2\2\u0156K\3\2\2\2\u0157\u0158")
        buf.write(u"\7,\2\2\u0158\u0159\7\5\2\2\u0159\u015a\5`\61\2\u015a")
        buf.write(u"\u015b\7\6\2\2\u015b\u015f\5:\36\2\u015c\u015e\5N(\2")
        buf.write(u"\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d")
        buf.write(u"\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0163\3\2\2\2\u0161")
        buf.write(u"\u015f\3\2\2\2\u0162\u0164\5P)\2\u0163\u0162\3\2\2\2")
        buf.write(u"\u0163\u0164\3\2\2\2\u0164M\3\2\2\2\u0165\u0166\7-\2")
        buf.write(u"\2\u0166\u0167\7\5\2\2\u0167\u0168\5`\61\2\u0168\u0169")
        buf.write(u"\7\6\2\2\u0169\u016a\5:\36\2\u016aO\3\2\2\2\u016b\u016c")
        buf.write(u"\7)\2\2\u016c\u016d\5:\36\2\u016dQ\3\2\2\2\u016e\u016f")
        buf.write(u"\5T+\2\u016f\u0170\7\t\2\2\u0170S\3\2\2\2\u0171\u0172")
        buf.write(u"\7\'\2\2\u0172\u0173\7\5\2\2\u0173\u0174\5^\60\2\u0174")
        buf.write(u"\u0175\7\6\2\2\u0175U\3\2\2\2\u0176\u0177\5X-\2\u0177")
        buf.write(u"\u0178\7\t\2\2\u0178W\3\2\2\2\u0179\u017a\7(\2\2\u017a")
        buf.write(u"\u017b\7\5\2\2\u017b\u0180\5f\64\2\u017c\u017d\7\b\2")
        buf.write(u"\2\u017d\u017f\5f\64\2\u017e\u017c\3\2\2\2\u017f\u0182")
        buf.write(u"\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write(u"\u0183\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184\7\6\2")
        buf.write(u"\2\u0184Y\3\2\2\2\u0185\u0186\5\\/\2\u0186\u0187\7\t")
        buf.write(u"\2\2\u0187[\3\2\2\2\u0188\u0189\5\u0082B\2\u0189\u018a")
        buf.write(u"\7\5\2\2\u018a\u018b\5^\60\2\u018b\u018c\7\6\2\2\u018c")
        buf.write(u"]\3\2\2\2\u018d\u0192\5`\61\2\u018e\u018f\7\b\2\2\u018f")
        buf.write(u"\u0191\5`\61\2\u0190\u018e\3\2\2\2\u0191\u0194\3\2\2")
        buf.write(u"\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0196")
        buf.write(u"\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u018d\3\2\2\2\u0195")
        buf.write(u"\u0196\3\2\2\2\u0196_\3\2\2\2\u0197\u0198\b\61\1\2\u0198")
        buf.write(u"\u0199\5t;\2\u0199\u019a\5`\61\16\u019a\u01a5\3\2\2\2")
        buf.write(u"\u019b\u01a5\5\\/\2\u019c\u01a5\5l\67\2\u019d\u01a5\5")
        buf.write(u"\36\20\2\u019e\u01a5\5\30\r\2\u019f\u01a5\5f\64\2\u01a0")
        buf.write(u"\u01a1\7\5\2\2\u01a1\u01a2\5`\61\2\u01a2\u01a3\7\6\2")
        buf.write(u"\2\u01a3\u01a5\3\2\2\2\u01a4\u0197\3\2\2\2\u01a4\u019b")
        buf.write(u"\3\2\2\2\u01a4\u019c\3\2\2\2\u01a4\u019d\3\2\2\2\u01a4")
        buf.write(u"\u019e\3\2\2\2\u01a4\u019f\3\2\2\2\u01a4\u01a0\3\2\2")
        buf.write(u"\2\u01a5\u01bc\3\2\2\2\u01a6\u01a7\f\r\2\2\u01a7\u01a8")
        buf.write(u"\5v<\2\u01a8\u01a9\5`\61\16\u01a9\u01bb\3\2\2\2\u01aa")
        buf.write(u"\u01ab\f\f\2\2\u01ab\u01ac\5x=\2\u01ac\u01ad\5`\61\r")
        buf.write(u"\u01ad\u01bb\3\2\2\2\u01ae\u01af\f\13\2\2\u01af\u01b0")
        buf.write(u"\5z>\2\u01b0\u01b1\5`\61\f\u01b1\u01bb\3\2\2\2\u01b2")
        buf.write(u"\u01b3\f\n\2\2\u01b3\u01b4\5|?\2\u01b4\u01b5\5`\61\13")
        buf.write(u"\u01b5\u01bb\3\2\2\2\u01b6\u01b7\f\t\2\2\u01b7\u01b8")
        buf.write(u"\5~@\2\u01b8\u01b9\5`\61\n\u01b9\u01bb\3\2\2\2\u01ba")
        buf.write(u"\u01a6\3\2\2\2\u01ba\u01aa\3\2\2\2\u01ba\u01ae\3\2\2")
        buf.write(u"\2\u01ba\u01b2\3\2\2\2\u01ba\u01b6\3\2\2\2\u01bb\u01be")
        buf.write(u"\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write(u"a\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\5d\63\2\u01c0")
        buf.write(u"\u01c1\7\t\2\2\u01c1c\3\2\2\2\u01c2\u01c3\5f\64\2\u01c3")
        buf.write(u"\u01c4\5\u0080A\2\u01c4\u01c5\5`\61\2\u01c5e\3\2\2\2")
        buf.write(u"\u01c6\u01ca\5\u0082B\2\u01c7\u01ca\5j\66\2\u01c8\u01ca")
        buf.write(u"\5h\65\2\u01c9\u01c6\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9")
        buf.write(u"\u01c8\3\2\2\2\u01cag\3\2\2\2\u01cb\u01cc\b\65\1\2\u01cc")
        buf.write(u"\u01cd\5\u0082B\2\u01cd\u01ce\7\f\2\2\u01ce\u01cf\5n")
        buf.write(u"8\2\u01cf\u01d0\7\r\2\2\u01d0\u01d8\3\2\2\2\u01d1\u01d2")
        buf.write(u"\f\4\2\2\u01d2\u01d3\7\f\2\2\u01d3\u01d4\5n8\2\u01d4")
        buf.write(u"\u01d5\7\r\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d1\3\2\2")
        buf.write(u"\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9")
        buf.write(u"\3\2\2\2\u01d9i\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01de")
        buf.write(u"\5\u0082B\2\u01dc\u01dd\7\16\2\2\u01dd\u01df\5j\66\2")
        buf.write(u"\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e2")
        buf.write(u"\3\2\2\2\u01e0\u01e2\5h\65\2\u01e1\u01db\3\2\2\2\u01e1")
        buf.write(u"\u01e0\3\2\2\2\u01e2k\3\2\2\2\u01e3\u01e7\5n8\2\u01e4")
        buf.write(u"\u01e7\5p9\2\u01e5\u01e7\5r:\2\u01e6\u01e3\3\2\2\2\u01e6")
        buf.write(u"\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7m\3\2\2\2\u01e8")
        buf.write(u"\u01e9\7\64\2\2\u01e9o\3\2\2\2\u01ea\u01eb\7\63\2\2\u01eb")
        buf.write(u"q\3\2\2\2\u01ec\u01ed\7\62\2\2\u01eds\3\2\2\2\u01ee\u01ef")
        buf.write(u"\t\2\2\2\u01efu\3\2\2\2\u01f0\u01f1\t\3\2\2\u01f1w\3")
        buf.write(u"\2\2\2\u01f2\u01f3\t\4\2\2\u01f3y\3\2\2\2\u01f4\u01f5")
        buf.write(u"\t\5\2\2\u01f5{\3\2\2\2\u01f6\u01f7\t\6\2\2\u01f7}\3")
        buf.write(u"\2\2\2\u01f8\u01f9\t\7\2\2\u01f9\177\3\2\2\2\u01fa\u01fb")
        buf.write(u"\t\b\2\2\u01fb\u0081\3\2\2\2\u01fc\u01fd\7\61\2\2\u01fd")
        buf.write(u"\u0083\3\2\2\2(\u0088\u008a\u0095\u00a1\u00a9\u00af\u00b3")
        buf.write(u"\u00bc\u00cc\u00d2\u00db\u00e6\u00ef\u00f8\u00fd\u010f")
        buf.write(u"\u0116\u011d\u012e\u0135\u0140\u0144\u0148\u014f\u0155")
        buf.write(u"\u015f\u0163\u0180\u0192\u0195\u01a4\u01ba\u01bc\u01c9")
        buf.write(u"\u01d8\u01de\u01e1\u01e6")
        return buf.getvalue()
		

class LLangParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"'('", u"')'", u"':'", 
                     u"','", u"';'", u"'='", u"'new'", u"'['", u"']'", u"'.'", 
                     u"'-'", u"'!'", u"'*'", u"'/'", u"'%'", u"'+'", u"'>'", 
                     u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", u"'&&'", 
                     u"'||'", u"'*='", u"'/='", u"'%='", u"'+='", u"'-='", 
                     u"'Bool'", u"'Int'", u"'Str'", u"'None'", u"'record'", 
                     u"'writeln'", u"'readln'", u"'else'", u"'for'", u"'while'", 
                     u"'if'", u"'elif'", u"'return'", u"'fun'", u"'pass'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"BOOL", u"INT", u"STR", u"NONE", u"RECORD", u"WRITELN", 
                      u"READLN", u"ELSE", u"FOR", u"WHILE", u"IF", u"ELIF", 
                      u"RETURN", u"FUN", u"PASS", u"Identifier", u"BooleanLiteral", 
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
    RULE_returnStatement = 30
    RULE_returnExpr = 31
    RULE_whileStatement = 32
    RULE_forStatement = 33
    RULE_forInit = 34
    RULE_forCondition = 35
    RULE_forUpdate = 36
    RULE_ifStatement = 37
    RULE_elifBlock = 38
    RULE_elseBlock = 39
    RULE_writelnStatement = 40
    RULE_writelnCall = 41
    RULE_readlnStatement = 42
    RULE_readlnCall = 43
    RULE_functionInvocationStatement = 44
    RULE_functionInvocation = 45
    RULE_argumentList = 46
    RULE_expression = 47
    RULE_assignmentStatement = 48
    RULE_assignment = 49
    RULE_leftHandSide = 50
    RULE_cortegeAccess = 51
    RULE_recordFieldAccess = 52
    RULE_literal = 53
    RULE_intLiteral = 54
    RULE_strLiteral = 55
    RULE_boolLiteral = 56
    RULE_unaryOperator = 57
    RULE_mulDivModOperator = 58
    RULE_addSubOperator = 59
    RULE_compareOperator = 60
    RULE_equalOrNotOperator = 61
    RULE_boolOperator = 62
    RULE_assignmentOperator = 63
    RULE_identifier = 64

    ruleNames =  [ u"programme", u"recordDeclaration", u"recordBody", u"functionDeclaration", 
                   u"functionSignature", u"functionReturnType", u"functionBody", 
                   u"functionParameterList", u"functionParameter", u"variableDeclarationStatement", 
                   u"variableDeclaration", u"recordInitializer", u"recordFieldInitializerList", 
                   u"recordFieldInitializer", u"cortegeInitializer", u"expressionList", 
                   u"passStatement", u"exprType", u"primitiveType", u"recordId", 
                   u"intType", u"strType", u"boolType", u"voidType", u"cortegeType", 
                   u"cortegeTypeUnit", u"cortegeTypeNonEmptyList", u"block", 
                   u"justBlock", u"statement", u"returnStatement", u"returnExpr", 
                   u"whileStatement", u"forStatement", u"forInit", u"forCondition", 
                   u"forUpdate", u"ifStatement", u"elifBlock", u"elseBlock", 
                   u"writelnStatement", u"writelnCall", u"readlnStatement", 
                   u"readlnCall", u"functionInvocationStatement", u"functionInvocation", 
                   u"argumentList", u"expression", u"assignmentStatement", 
                   u"assignment", u"leftHandSide", u"cortegeAccess", u"recordFieldAccess", 
                   u"literal", u"intLiteral", u"strLiteral", u"boolLiteral", 
                   u"unaryOperator", u"mulDivModOperator", u"addSubOperator", 
                   u"compareOperator", u"equalOrNotOperator", u"boolOperator", 
                   u"assignmentOperator", u"identifier" ]

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
    BOOL=32
    INT=33
    STR=34
    NONE=35
    RECORD=36
    WRITELN=37
    READLN=38
    ELSE=39
    FOR=40
    WHILE=41
    IF=42
    ELIF=43
    RETURN=44
    FUN=45
    PASS=46
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
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.RECORD) | (1 << LLangParser.FUN) | (1 << LLangParser.Identifier))) != 0):
                self.state = 134
                token = self._input.LA(1)
                if token in [LLangParser.T__9, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                    self.state = 130 
                    self.variableDeclarationStatement()

                elif token in [LLangParser.FUN]:
                    self.state = 131 
                    self.functionDeclaration()

                elif token in [LLangParser.RECORD]:
                    self.state = 132 
                    self.recordDeclaration()

                elif token in [LLangParser.T__0]:
                    self.state = 133 
                    self.justBlock()

                else:
                    raise NoViableAltException(self)

                self.state = 138
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
            self.state = 139
            self.match(LLangParser.RECORD)
            self.state = 140 
            self.recordId()
            self.state = 141 
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
            self.state = 143
            self.match(LLangParser.T__0)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.Identifier))) != 0):
                self.state = 144 
                self.variableDeclarationStatement()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
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
            self.state = 152
            self.match(LLangParser.FUN)
            self.state = 153 
            self.functionSignature()
            self.state = 154 
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
            self.state = 156 
            self.identifier()
            self.state = 157
            self.match(LLangParser.T__2)
            self.state = 159
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 158 
                self.functionParameterList()


            self.state = 161
            self.match(LLangParser.T__3)
            self.state = 162
            self.match(LLangParser.T__4)
            self.state = 163 
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
            self.state = 167
            token = self._input.LA(1)
            if token in [LLangParser.T__9, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165 
                self.exprType()

            elif token in [LLangParser.NONE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166 
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
            self.state = 169
            self.match(LLangParser.T__0)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 170 
                self.statement()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            _la = self._input.LA(1)
            if _la==LLangParser.RETURN:
                self.state = 176 
                self.returnStatement()


            self.state = 179
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
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 181 
                    self.functionParameter()
                    self.state = 182
                    self.match(LLangParser.T__5) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 189 
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
            self.state = 191 
            self.identifier()
            self.state = 192
            self.match(LLangParser.T__4)
            self.state = 193 
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
            self.state = 195 
            self.variableDeclaration()
            self.state = 196
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
            self.state = 198 
            self.exprType()
            self.state = 199 
            self.identifier()
            self.state = 202
            _la = self._input.LA(1)
            if _la==LLangParser.T__7:
                self.state = 200
                self.match(LLangParser.T__7)
                self.state = 201 
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
            self.state = 204
            self.match(LLangParser.T__8)
            self.state = 205 
            self.identifier()
            self.state = 206
            self.match(LLangParser.T__2)
            self.state = 208
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 207 
                self.recordFieldInitializerList()


            self.state = 210
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
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 212 
                    self.recordFieldInitializer()
                    self.state = 213
                    self.match(LLangParser.T__5) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 220 
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
            self.state = 222 
            self.identifier()
            self.state = 223
            self.match(LLangParser.T__7)
            self.state = 224 
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
            self.state = 226
            self.match(LLangParser.T__9)
            self.state = 228
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 227 
                self.expressionList()


            self.state = 230
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
            self.state = 232 
            self.expression(0)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 233
                self.match(LLangParser.T__5)
                self.state = 234 
                self.expression(0)
                self.state = 239
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
            self.state = 240
            self.match(LLangParser.PASS)
            self.state = 241
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
            self.state = 246
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243 
                self.primitiveType()

            elif token in [LLangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244 
                self.cortegeType()

            elif token in [LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 245 
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
            self.state = 251
            token = self._input.LA(1)
            if token in [LLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248 
                self.intType()

            elif token in [LLangParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249 
                self.strType()

            elif token in [LLangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 250 
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
            self.state = 253
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
            self.state = 255
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
            self.state = 257
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
            self.state = 259
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
            self.state = 261
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
            self.state = 263
            self.match(LLangParser.T__9)
            self.state = 264 
            self.cortegeTypeNonEmptyList()
            self.state = 265
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
            self.state = 269
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267 
                self.primitiveType()

            elif token in [LLangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268 
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
            self.state = 271 
            self.cortegeTypeUnit()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 272
                self.match(LLangParser.T__5)
                self.state = 273 
                self.cortegeTypeUnit()
                self.state = 278
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
            self.state = 279
            self.match(LLangParser.T__0)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 280 
                self.statement()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 286
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
            self.state = 288 
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
            self.state = 300
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290 
                self.justBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291 
                self.variableDeclarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 292 
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 293 
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 294 
                self.functionInvocationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 295 
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 296 
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 297 
                self.passStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 298 
                self.readlnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 299 
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
        self.enterRule(localctx, 60, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302 
            self.returnExpr()
            self.state = 303
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
        self.enterRule(localctx, 62, self.RULE_returnExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(LLangParser.RETURN)
            self.state = 307
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 306 
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
        self.enterRule(localctx, 64, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(LLangParser.WHILE)
            self.state = 310
            self.match(LLangParser.T__2)
            self.state = 311 
            self.expression(0)
            self.state = 312
            self.match(LLangParser.T__3)
            self.state = 313 
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


        def forCondition(self):
            return self.getTypedRuleContext(LLangParser.ForConditionContext,0)


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
        self.enterRule(localctx, 66, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(LLangParser.FOR)
            self.state = 316
            self.match(LLangParser.T__2)
            self.state = 318
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.Identifier))) != 0):
                self.state = 317 
                self.forInit()


            self.state = 320
            self.match(LLangParser.T__6)
            self.state = 322
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 321 
                self.forCondition()


            self.state = 324
            self.match(LLangParser.T__6)
            self.state = 326
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 325 
                self.forUpdate()


            self.state = 328
            self.match(LLangParser.T__3)
            self.state = 329 
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
        self.enterRule(localctx, 68, self.RULE_forInit)
        try:
            self.state = 333
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332 
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
        self.enterRule(localctx, 70, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335 
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
        self.enterRule(localctx, 72, self.RULE_forUpdate)
        try:
            self.state = 339
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338 
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
        self.enterRule(localctx, 74, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(LLangParser.IF)
            self.state = 342
            self.match(LLangParser.T__2)
            self.state = 343 
            self.expression(0)
            self.state = 344
            self.match(LLangParser.T__3)
            self.state = 345 
            self.justBlock()
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.ELIF:
                self.state = 346 
                self.elifBlock()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 353
            _la = self._input.LA(1)
            if _la==LLangParser.ELSE:
                self.state = 352 
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
        self.enterRule(localctx, 76, self.RULE_elifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(LLangParser.ELIF)
            self.state = 356
            self.match(LLangParser.T__2)
            self.state = 357 
            self.expression(0)
            self.state = 358
            self.match(LLangParser.T__3)
            self.state = 359 
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
        self.enterRule(localctx, 78, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(LLangParser.ELSE)
            self.state = 362 
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
        self.enterRule(localctx, 80, self.RULE_writelnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364 
            self.writelnCall()
            self.state = 365
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
        self.enterRule(localctx, 82, self.RULE_writelnCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(LLangParser.WRITELN)
            self.state = 368
            self.match(LLangParser.T__2)
            self.state = 369 
            self.argumentList()
            self.state = 370
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
        self.enterRule(localctx, 84, self.RULE_readlnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372 
            self.readlnCall()
            self.state = 373
            self.match(LLangParser.T__6)
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
        self.enterRule(localctx, 86, self.RULE_readlnCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(LLangParser.READLN)
            self.state = 376
            self.match(LLangParser.T__2)
            self.state = 377 
            self.leftHandSide()
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 378
                self.match(LLangParser.T__5)
                self.state = 379 
                self.leftHandSide()
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 385
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
        self.enterRule(localctx, 88, self.RULE_functionInvocationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387 
            self.functionInvocation()
            self.state = 388
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
        self.enterRule(localctx, 90, self.RULE_functionInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390 
            self.identifier()
            self.state = 391
            self.match(LLangParser.T__2)
            self.state = 392 
            self.argumentList()
            self.state = 393
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
        self.enterRule(localctx, 92, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 395 
                self.expression(0)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LLangParser.T__5:
                    self.state = 396
                    self.match(LLangParser.T__5)
                    self.state = 397 
                    self.expression(0)
                    self.state = 402
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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 406 
                self.unaryOperator()
                self.state = 407 
                self.expression(12)
                pass

            elif la_ == 2:
                self.state = 409 
                self.functionInvocation()
                pass

            elif la_ == 3:
                self.state = 410 
                self.literal()
                pass

            elif la_ == 4:
                self.state = 411 
                self.cortegeInitializer()
                pass

            elif la_ == 5:
                self.state = 412 
                self.recordInitializer()
                pass

            elif la_ == 6:
                self.state = 413 
                self.leftHandSide()
                pass

            elif la_ == 7:
                self.state = 414
                self.match(LLangParser.T__2)
                self.state = 415 
                self.expression(0)
                self.state = 416
                self.match(LLangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 440
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 420
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 421 
                        self.mulDivModOperator()
                        self.state = 422 
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 424
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 425 
                        self.addSubOperator()
                        self.state = 426 
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 428
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 429 
                        self.compareOperator()
                        self.state = 430 
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 432
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 433 
                        self.equalOrNotOperator()
                        self.state = 434 
                        self.expression(9)
                        pass

                    elif la_ == 5:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 436
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 437 
                        self.boolOperator()
                        self.state = 438 
                        self.expression(8)
                        pass

             
                self.state = 444
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
        self.enterRule(localctx, 96, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445 
            self.assignment()
            self.state = 446
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
        self.enterRule(localctx, 98, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448 
            self.leftHandSide()
            self.state = 449 
            self.assignmentOperator()
            self.state = 450 
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
        self.enterRule(localctx, 100, self.RULE_leftHandSide)
        try:
            self.state = 455
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452 
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453 
                self.recordFieldAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454 
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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_cortegeAccess, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458 
            self.identifier()
            self.state = 459
            self.match(LLangParser.T__9)
            self.state = 460 
            self.intLiteral()
            self.state = 461
            self.match(LLangParser.T__10)
            self._ctx.stop = self._input.LT(-1)
            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LLangParser.CortegeAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cortegeAccess)
                    self.state = 463
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 464
                    self.match(LLangParser.T__9)
                    self.state = 465 
                    self.intLiteral()
                    self.state = 466
                    self.match(LLangParser.T__10) 
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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




    def recordFieldAccess(self):

        localctx = LLangParser.RecordFieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_recordFieldAccess)
        try:
            self.state = 479
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473 
                self.identifier()
                self.state = 476
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 474
                    self.match(LLangParser.T__11)
                    self.state = 475 
                    self.recordFieldAccess()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478 
                self.cortegeAccess(0)
                pass


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
        self.enterRule(localctx, 106, self.RULE_literal)
        try:
            self.state = 484
            token = self._input.LA(1)
            if token in [LLangParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481 
                self.intLiteral()

            elif token in [LLangParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482 
                self.strLiteral()

            elif token in [LLangParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 483 
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
        self.enterRule(localctx, 108, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
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
        self.enterRule(localctx, 110, self.RULE_strLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
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
        self.enterRule(localctx, 112, self.RULE_boolLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
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
        self.enterRule(localctx, 114, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__12 or _la==LLangParser.T__13):
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
        self.enterRule(localctx, 116, self.RULE_mulDivModOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__14) | (1 << LLangParser.T__15) | (1 << LLangParser.T__16))) != 0)):
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
        self.enterRule(localctx, 118, self.RULE_addSubOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__12 or _la==LLangParser.T__17):
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
        self.enterRule(localctx, 120, self.RULE_compareOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__18) | (1 << LLangParser.T__19) | (1 << LLangParser.T__20) | (1 << LLangParser.T__21))) != 0)):
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
        self.enterRule(localctx, 122, self.RULE_equalOrNotOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__22 or _la==LLangParser.T__23):
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
        self.enterRule(localctx, 124, self.RULE_boolOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__24 or _la==LLangParser.T__25):
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
        self.enterRule(localctx, 126, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__7) | (1 << LLangParser.T__26) | (1 << LLangParser.T__27) | (1 << LLangParser.T__28) | (1 << LLangParser.T__29) | (1 << LLangParser.T__30))) != 0)):
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
        self.enterRule(localctx, 128, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
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
        self._predicates[47] = self.expression_sempred
        self._predicates[51] = self.cortegeAccess_sempred
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
         

    def cortegeAccess_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         



