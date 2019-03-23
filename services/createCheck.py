def createCheckAuthor(ctx):
    def check(m):
        return m.author == ctx.author
    
    return check