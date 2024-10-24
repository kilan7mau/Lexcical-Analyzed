class Token:
    def __init__(self, lexeme, token_type):
        self.lexeme = lexeme
        self.token_type = token_type

    def __str__(self):
        return f"{self.lexeme} : {self.token_type}"

def tokenize(code):
    tokens = []
    i = 0

    # Danh sách từ khóa, hàm có sẵn, toán tử, ký tự đặc biệt và dấu phân cách
    keywords = ['break','case','char','const','continue','default','do','int','else','enum','extern','float','for','goto','if','long','register','return','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while']
    built_in_functions = ['clrscr()', 'printf(', 'scanf(', 'getch()', 'main()']
    operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~', '>>', '<<', '=', '+=', '-=', '*=']
    specialsymbol = ['@', '#', '$', '_', '!']
    separators = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']

    while i < len(code):
        char = code[i]

        # Bỏ qua khoảng trắng
        if char.isspace():
            i += 1
            continue

        # Xử lý từ khóa, định danh và hàm built-in
        if char.isalpha() or char == '_':
            lexeme = ''
            while i < len(code) and (code[i].isalnum() or code[i] == '_'):
                lexeme += code[i]
                i += 1
            if lexeme in keywords:
                tokens.append(Token(lexeme, 'keyword'))
            elif lexeme + '()' in built_in_functions:  # Kiểm tra hàm built-in
                tokens.append(Token(lexeme + '()', 'built-in_function'))
            else:
                tokens.append(Token(lexeme, 'identifier'))
            continue

        # Xử lý số
        if char.isdigit():
            lexeme = ''
            while i < len(code) and (code[i].isdigit() or code[i] == '.'):
                lexeme += code[i]
                i += 1
            tokens.append(Token(lexeme, 'num'))
            continue

        # Xử lý toán tử
        if code[i:i+2] in operators:  # Toán tử 2 ký tự
            tokens.append(Token(code[i:i+2], 'operator'))
            i += 2
        elif char in operators:  # Toán tử 1 ký tự
            tokens.append(Token(char, 'operator'))
            i += 1
            continue

        # Xử lý dấu phân cách
        if char in separators:
            tokens.append(Token(char, 'separator'))
            i += 1
            continue

        # Xử lý ký tự đặc biệt
        if char in specialsymbol:
            tokens.append(Token(char, 'special_symbol'))
            i += 1
            continue

        # Xử lý lỗi
        tokens.append(Token(char, 'Error'))
        i += 1

    return tokens

def main():
    # Đọc file
    with open('input.txt', 'r') as file:
        code = file.read()

    # Phân tích từ vựng
    tokens = tokenize(code)

    # In kết quả theo định dạng yêu cầu
    for token in tokens:
        print(token)

if __name__ == '__main__':
    main()
