#đọc file word -> json
import os
import json
import re
from tkinter import Tk, filedialog, messagebox
from docx import Document

def is_highlighted(run):
    """Kiểm tra xem một run có được tô sáng màu vàng hay không."""
    return run.font.highlight_color == 7 if run.font.highlight_color else False

def parse_questions(doc_path):
    document = Document(doc_path)
    questions = []
    question = {}
    answers = []
    question_number = 1
    question_pattern = re.compile(r'^\d+\)')  #nhận dạng câu hỏi
    answer_pattern = re.compile(r'^[ABCD]\.')  
    
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue
        if question_pattern.match(text):  
            if question:  
                question['answers'] = answers
                questions.append(question)
                question = {}
                answers = []
            question_text = text.split(')', 1)[1].strip()
            question['question_number'] = question_number
            question['question_text'] = question_text
            question_number += 1
        elif answer_pattern.match(text):  # Phát hiện câu trả lời
            correct = any(is_highlighted(run) for run in paragraph.runs)
            answers.append({
                "text": text[2:].strip(),
                "correct": correct
            })
    if question:  # Thêm câu hỏi cuối cùng
        question['answers'] = answers
        questions.append(question)
    return questions

def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Chọn một tập tin Word",
        filetypes=[("Word Documents", "*.docx")]
    )

    if not file_path:
        messagebox.showinfo("Không có file nào được chọn", "Bạn chưa chọn file.")
        return

    try:
        questions_data = parse_questions(file_path)

        if not questions_data:
            messagebox.showwarning("Không có dữ liệu", "Không tìm thấy câu hỏi hoặc đáp án trong file.")
            return

        output_path = filedialog.asksaveasfilename(
            title="Lưu tập tin JSON",
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json")]
        )

        if not output_path:
            messagebox.showinfo("Hủy lưu file", "Bạn đã hủy lưu file.")
            return

        save_to_json(questions_data, output_path)
        messagebox.showinfo("Thành công", f"Dữ liệu JSON đã được lưu tại {output_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")

if __name__ == "__main__":
    main()
