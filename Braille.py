def braille(params):
    if params == [
        0, 0,
        0, 0,
        0, 0
    ]:
        return '⠀'
    if params == [
        1, 0,
        0, 0,
        0, 0
    ]:
        return '⠂'
    if params == [
        0, 0,
        1, 0,
        0, 0
    ]:
        return '⠂'
    if params == [
        1, 0,
        1, 0,
        0, 0
    ]:
        return '⠃'
    if params == [
        0, 0,
        0, 0,
        1, 0
    ]:
        return '⠄'
    if params == [
        1, 0,
        0, 0,
        1, 0
    ]:
        return '⠅'
    if params == [
        0, 0,
        1, 0,
        1, 0
    ]:
        return '⠆'
    if params == [
        1, 0,
        1, 0,
        1, 0
    ]:
        return '⠇'
    if params == [
        0, 1,
        0, 0,
        0, 0
    ]:
        return '⠈'
    if params == [
        1, 1,
        0, 0,
        0, 0
    ]:
        return '⠉'
    if params == [
        0, 1,
        1, 0,
        0, 0
    ]:
        return '⠊'
    if params == [
        1, 1,
        1, 0,
        0, 0
    ]:
        return '⠋'
    if params == [
        0, 1,
        0, 0,
        1, 0
    ]:
        return '⠌'
    if params == [
        1, 1,
        0, 0,
        1, 0
    ]:
        return '⠍'
    if params == [
        0, 1,
        1, 0,
        1, 0
    ]:
        return '⠎'
    if params == [
        1, 1,
        1, 0,
        1, 0
    ]:
        return '⠏'
    if params == [
        0, 0,
        0, 1,
        0, 0
    ]:
        return '⠐'
    if params == [
        1, 0,
        0, 1,
        0, 0
    ]:
        return '⠑'
    if params == [
        0, 0,
        1, 1,
        0, 0
    ]:
        return '⠒'
    if params == [
        1, 0,
        1, 1,
        0, 0
    ]:
        return '⠓'
    if params == [
        0, 0,
        0, 1,
        1, 0
    ]:
        return '⠔'
    if params == [
        1, 0,
        0, 1,
        1, 0
    ]:
        return '⠕'
    if params == [
        0, 0,
        1, 1,
        1, 0
    ]:
        return '⠖'
    if params == [
        1, 0,
        1, 1,
        1, 0
    ]:
        return '⠗'
    if params == [
        0, 1,
        0, 1,
        0, 0
    ]:
        return '⠘'
    if params == [
        1, 1,
        0, 1,
        0, 0
    ]:
        return '⠙'
    if params == [
        0, 1,
        1, 1,
        0, 0
    ]:
        return '⠚'
    if params == [
        1, 1,
        1, 1,
        0, 0
    ]:
        return '⠛'
    if params == [
        0, 1,
        0, 1,
        1, 0
    ]:
        return '⠜'
    if params == [
        1, 1,
        0, 1,
        1, 0
    ]:
        return '⠝'
    if params == [
        0, 1,
        1, 1,
        1, 0
    ]:
        return '⠞'
    if params == [
        1, 1,
        1, 1,
        1, 0
    ]:
        return '⠟'
    if params == [
        0, 0,
        0, 0,
        0, 1
    ]:
        return '⠠'
    if params == [
        1, 0,
        0, 0,
        0, 1
    ]:
        return '⠡'
    if params == [
        0, 0,
        1, 0,
        0, 1
    ]:
        return '⠢'
    if params == [
        1, 0,
        1, 0,
        0, 1
    ]:
        return '⠣'
    if params == [
        0, 0,
        0, 0,
        1, 1
    ]:
        return '⠤'
    if params == [
        1, 0,
        0, 0,
        1, 1
    ]:
        return '⠥'
    if params == [
        0, 0,
        1, 0,
        1, 1
    ]:
        return '⠦'
    if params == [
        1, 0,
        1, 0,
        1, 1
    ]:
        return '⠧'
    if params == [
        0, 1,
        0, 0,
        0, 1
    ]:
        return '⠨'
    if params == [
        1, 1,
        0, 0,
        0, 1
    ]:
        return '⠩'
    if params == [
        0, 1,
        1, 0,
        0, 1
    ]:
        return '⠪'
    if params == [
        1, 1,
        1, 0,
        0, 1
    ]:
        return '⠫'
    if params == [
        0, 1,
        0, 0,
        1, 1
    ]:
        return '⠬'
    if params == [
        1, 1,
        0, 0,
        1, 1
    ]:
        return '⠭'
    if params == [
        0, 1,
        1, 0,
        1, 1
    ]:
        return '⠮'
    if params == [
        1, 1,
        1, 0,
        1, 1
    ]:
        return '⠯'
    if params == [
        0, 0,
        0, 1,
        0, 1
    ]:
        return '⠰'
    if params == [
        1, 0,
        0, 1,
        0, 1
    ]:
        return '⠱'
    if params == [
        0, 0,
        1, 1,
        0, 1
    ]:
        return '⠲'
    if params == [
        1, 0,
        1, 1,
        0, 1
    ]:
        return '⠳'
    if params == [
        0, 0,
        0, 1,
        1, 1
    ]:
        return '⠴'
    if params == [
        1, 0,
        0, 1,
        1, 1
    ]:
        return '⠵'
    if params == [
        0, 0,
        1, 1,
        1, 1
    ]:
        return '⠶'
    if params == [
        1, 0,
        1, 1,
        1, 1
    ]:
        return '⠷'
    if params == [
        0, 1,
        0, 1,
        0, 1
    ]:
        return '⠸'
    if params == [
        1, 1,
        0, 1,
        0, 1
    ]:
        return '⠹'
    if params == [
        0, 1,
        1, 1,
        0, 1
    ]:
        return '⠺'
    if params == [
        1, 1,
        1, 1,
        0, 1
    ]:
        return '⠻'
    if params == [
        0, 1,
        0, 1,
        1, 1
    ]:
        return '⠼'
    if params == [
        1, 1,
        0, 1,
        1, 1
    ]:
        return '⠽'
    if params == [
        0, 1,
        1, 1,
        1, 1
    ]:
        return '⠾'
    if params == [
        1, 1,
        1, 1,
        1, 1
    ]:
        return '⠿'
    return '⠒'
