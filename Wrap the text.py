import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    paragraph = wrapper.wrap(text = string)
    noList = ''
    for words in paragraph:
        noList = noList + words + '\n'
    return noList

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
