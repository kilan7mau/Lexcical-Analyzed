# Lớp Token lưu trữ thông tin về token và định dạng đầu ra của token
class Token:
    def __init__(self, lexeme, token_type):
        self.lexeme = lexeme  # Chuỗi ký tự (lexeme) của token
        self.token_type = token_type  # Loại của token (từ khóa, định danh, số, etc.)

    # Định dạng để in token ra màn hình
    def __str__(self):
        return f"{self.token_type} : {self.lexeme}"

# Hàm phân tích từ vựng từ đoạn mã nguồn
def tokenize(code):
    tokens = []  # Danh sách chứa các token
    i = 0  # Chỉ số hiện tại trong chuỗi mã nguồn

    # Danh sách từ khóa của ngôn ngữ lập trình
    keywords = ['break', 'case', 'char', 'const', 'continue', 'default', 'do', 'int', 'else', 'enum', 'extern',
                'float', 'for', 'goto', 'if', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 
                'static', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

    # Danh sách các toán tử
    operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '=', '+=', '-=', '*=']

    # Danh sách các dấu phân cách
    separators = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']

    # Bắt đầu vòng lặp để phân tích từng ký tự trong đoạn mã
    while i < len(code):
        char = code[i]

        # Bỏ qua khoảng trắng
        if char.isspace():
            i += 1
            continue

        # Xử lý định danh và từ khóa
        if char.isalpha() or char == '_':
            lexeme = ''
            # Thu thập toàn bộ chuỗi định danh hoặc từ khóa
            while i < len(code) and (code[i].isalnum() or code[i] == '_'):
                lexeme += code[i]
                i += 1
            # Kiểm tra xem đó là từ khóa hay định danh
            if lexeme in keywords:
                tokens.append(Token(lexeme, 'keyword'))
            else:
                tokens.append(Token(lexeme, 'identifier'))
            continue

        # Xử lý số (bao gồm cả số thực)
        if char.isdigit():
            lexeme = ''
            has_dot = False  # Kiểm tra có dấu chấm thập phân
            has_e = False    # Kiểm tra có kí hiệu số mũ e/E
            while i < len(code) and (code[i].isdigit() or code[i] in '.eE'):
                if code[i] == '.' and not has_dot:
                    has_dot = True
                elif code[i] in 'eE' and not has_e:
                    has_e = True
                    lexeme += code[i]
                    i += 1
                    if code[i] in '+-':  # Xử lý e+, e- trong số mũ
                        lexeme += code[i]
                        i += 1
                    continue
                lexeme += code[i]
                i += 1
            tokens.append(Token(lexeme, 'num'))
            continue

        # Xử lý các toán tử (kiểm tra toán tử có thể là 2 ký tự trước, sau đó là 1 ký tự)
        if code[i:i+2] in operators:  # Toán tử hai ký tự
            tokens.append(Token(code[i:i+2], 'operator'))
            i += 2
            continue
        elif char in operators:  # Toán tử một ký tự
            tokens.append(Token(char, 'operator'))
            i += 1
            continue

        # Xử lý các dấu phân cách
        if char in separators:
            tokens.append(Token(char, char))
            i += 1
            continue

        # Nếu không thuộc loại nào, token đó là lỗi
        tokens.append(Token(char, 'Error'))
        i += 1

    return tokens

# Hàm main để thực thi chương trình
def main():
    # Đọc nội dung file 'input.txt'
    with open('input.txt', 'r') as file:
        code = file.read()

    # Gọi hàm tokenize để phân tích và thu thập các token
    tokens = tokenize(code)

    # In từng token ra màn hình theo định dạng yêu cầu
    print("Class : Lexeme")
    for token in tokens:
        print(token)

# Điểm bắt đầu của chương trình
if __name__ == '__main__':
    main()
