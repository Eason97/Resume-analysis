import os
import docx
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from tkinter import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
def getContet(file_name, pages=None):
    if (file_name is None):
        return
    print(file_name)
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(file_name, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    result = []
    for line in text.split('\n'):
        line2 = line.strip()
        if line2 != '':
            result.append(line2)
    return result
def preprocess_text(text):
    text = ' '.join(text.split())
    text = join_name(text)
    return text
def join_name(text):
    text = text.replace('\u2003', '')
    return text
def main():
    print(preprocess_text('name'))
if __name__ == '__main__':
    main()
def docx_to_text(file_path):
    doc = docx.Document(file_path)
    result = []
    for p in doc.paragraphs:
        txt = p.text.strip()
        if txt != '':
            txt = preprocess_text(txt)
            result.append(txt)
    return result
def read_pdf_and_docx(dir_path, collected=None, command_logging=False, callback=None):
    if collected is None:
        collected = dict()
    for f in os.listdir(dir_path):
        file_path = os.path.join(dir_path, f)
        if os.path.isfile(file_path):
            txt = None
            if f.lower().endswith('.docx'):
                if command_logging:
                    print('extracting text from docx: ', file_path)
                txt = docx_to_text(file_path)
            elif f.lower().endswith('.pdf'):
                if command_logging:
                    print('extracting text from pdf: ', file_path)
                txt = getContet(file_path)
            if txt is not None and len(txt) > 0:
                if callback is not None:
                    callback(len(collected), file_path, txt)
                collected[file_path] = txt
        elif os.path.isdir(file_path):
            read_pdf_and_docx(file_path, collected, command_logging, callback)
    return collected
class Interface(Frame):
    def __init__(self, master, rank):
        Frame.__init__(self, master=master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W+E+N+S)
        for line_index, line in enumerate(rank):
            self.build_line(rank, line_index, line)
    def build_line(self, table_content, line_index, line):
        line_content = line[0]
        line_index_label = Label(self, width=3, height=1, text=str(line_index))
        line_index_label.grid(row=line_index, column=0, sticky=W + E + N + S)
        line_content_text = Text(self, width=100,height=1)
        line_content_text.insert(INSERT, line_content)
        line_content_text.grid(row=line_index, column=1, sticky=W + E + N + S)
        def analysis_button_click(_line_index):
            table_content[_line_index][1] = "analysis"
            analysis_button.config(state="disabled")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def communication_button_click(_line_index):
            table_content[_line_index][1] = "communication"
            analysis_button.config(state="normal")
            communication_button.config(state="disabled")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def organization_button_click(_line_index):
            table_content[_line_index][1] = "organization"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="disabled")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def problem_solving_button_click(_line_index):
            table_content[_line_index][1] = "problem solving"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="disabled")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def team_work_button_click(_line_index):
            table_content[_line_index][1] = "team work"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="disabled")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def industry_knowledge_button_click(_line_index):
            table_content[_line_index][1] = "industry knowledge"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="disabled")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def multitask_button_click(_line_index):
            table_content[_line_index][1] = "multitask"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="disabled")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def leadership_button_click(_line_index):
            table_content[_line_index][1] = "leadership"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="disabled")
            none_button.config(state="normal")
            company_button.config(state="normal")
        def none_button_click(_line_index):
            table_content[_line_index][1] = "none"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="disabled")
            company_button.config(state="normal")
        def company_button_click(_line_index):
            table_content[_line_index][1] = "none"
            analysis_button.config(state="normal")
            communication_button.config(state="normal")
            organization_button.config(state="normal")
            problem_solving_button.config(state="normal")
            team_work_button.config(state="normal")
            industry_knowledge_button.config(state="normal")
            multitask_button.config(state="normal")
            leadership_button.config(state="normal")
            none_button.config(state="normal")
            company_button.config(state="disabled")

        analysis_button = Button(self, text="Ana", width=2, command=lambda: analysis_button_click(line_index))
        analysis_button.grid(row=line_index, column=2, sticky=W + E + N + S)
        communication_button = Button(self, text='Com', width=2, command=lambda: communication_button_click(line_index))
        communication_button.grid(row=line_index, column=3, sticky=W + E + N + S)
        organization_button = Button(self, text='Org', width=2, command=lambda: organization_button_click(line_index))
        organization_button.grid(row=line_index, column=4, sticky=W + E + N + S)
        problem_solving_button = Button(self, text='Pro S', width=4, command=lambda: problem_solving_button_click(line_index))
        problem_solving_button.grid(row=line_index, column=5, sticky=W + E + N + S)
        team_work_button = Button(self, text="T M", width=2, command=lambda: team_work_button_click(line_index))
        team_work_button.grid(row=line_index, column=6, sticky=W + E + N + S)
        industry_knowledge_button = Button(self, text='Ind K', width=4, command=lambda: industry_knowledge_button_click(line_index))
        industry_knowledge_button.grid(row=line_index, column=7, sticky=W + E + N + S)
        multitask_button = Button(self, text='Mul', width=2, command=lambda: multitask_button_click(line_index))
        multitask_button.grid(row=line_index, column=8, sticky=W + E + N + S)
        leadership_button = Button(self, text='Lead', width=2, command=lambda: leadership_button_click(line_index))
        leadership_button.grid(row=line_index, column=9, sticky=W + E + N + S)
        none_button = Button(self, text='None', width=2, command=lambda: none_button_click(line_index))
        none_button.grid(row=line_index, column=10, sticky=W + E + N + S)
        company_button = Button(self, text='company', width=4, command=lambda: company_button_click(line_index))
        company_button.grid(row=line_index, column=11, sticky=W + E + N + S)

def category(line):
        return -1
def CanV_annotate(dataset_dir_path, index, file_path, file_content):
    root = Tk()
    table_content = [[line, category(line)] for line in file_content]
    root.title("Resume")
    root.geometry("1440x920+100+100")
    CanV = Interface(root, table_content)
    table_content = [[line, category(line)] for line in file_content]
    canvas = Canvas(width=10000, height=920,bg = "white", scrollregion=(0, 0,8000, 8000))  
    canvas.place(x=0, y=0)
    frame = Interface(canvas, table_content)
    vbar = Scrollbar(canvas, orient=VERTICAL)
    vbar.place(x=1325, width=20, height=920)
    vbar.configure(command=canvas.yview)
    canvas.config(yscrollcommand=vbar.set)
    canvas.create_window((0,0), window=frame,anchor =N+W)
    def callback():
        root.destroy()
        output_file_path = os.path.join(dataset_dir_path, str(index) + '.txt')
        if os.path.exists(output_file_path):
            return
        with open(output_file_path, 'wt', encoding='utf8') as f:
            for line in table_content:
                line_content = line[0]
                categorys= line[1]
                if categorys== -1:
                    continue
                print('write line: ', line)
                f.write(str(categorys) + '\t' + line_content)
                f.write('\n')
    root.protocol("WM_DELETE_WINDOW", callback)
    frame.mainloop()
def main():
    current_dir = os.path.dirname(__file__)
    current_dir = current_dir if current_dir is not '' else '.'
    data_dir_path = current_dir + '/data'
    dataset_dir_path = current_dir + '/data/dataset'
    collected = read_pdf_and_docx(data_dir_path, command_logging=True, callback=lambda index, file_path, file_content: {
        CanV_annotate(dataset_dir_path, index, file_path, file_content)
    })
    print('count: ', len(collected))
if __name__ == '__main__':
    main()
