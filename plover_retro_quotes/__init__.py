def retro_quotes(ctx, cmdline, quote_char):
    action = ctx.copy_last_action()

    num_words_to_quote = int(cmdline)

    last_words = "".join(ctx.last_words(count=num_words_to_quote))
    action.prev_replace = last_words
    action.text = quote_char + last_words + quote_char
    action.word = None
    action.prev_attach = True

    return action


def retro_single_quotes(*args, **kwargs):
    return retro_quotes(*args, **kwargs, quote_char="'")


def retro_double_quotes(*args, **kwargs):
    return retro_quotes(*args, **kwargs, quote_char='"')
