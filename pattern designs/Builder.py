class ReportBuilder:
    def __init__(self):
        self.report = {'title': "",
                       'date': "",
                       'content': ""}

    def set_title(self, title):
        self.report['title'] = title
        return self

    def set_date(self, date):
        self.report["date"] = date
        return self

    def set_content(self, content):
        self.report['content'] = content
        return self

    def build(self):
        return self.report


builder = ReportBuilder()

report = builder.set_title("Python analiz")\
    .set_date("16.02.2026")\
    .set_content("This is a content of report!")\
    .build()


print('report details: ', report)
