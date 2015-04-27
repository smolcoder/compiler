def capitalizeFirst(s):
    return s[0].capitalize() + s[1:]


def getRuleName(ctx):
    return ctx.parser.ruleNames[ctx.getRuleIndex()]