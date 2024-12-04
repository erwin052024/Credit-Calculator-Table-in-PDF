
import re
import tabulate
from fpdf import FPDF
import os

# KALKULATOR KREDYTOWY Z Tabulate i plikiem pdf

def main():
    #notatka informacyjna na początek
    print(introductioninformation())
   
    creditamount = correct_creditamount()
    annualinterestrateonthecredit = correct_annualinterestrate()
    monthlyinterestrateonthecredit = calculatethemonthlyinterestrate(annualinterestrateonthecredit)
    creditterm = correct_creditterm()
    numberofpaymentperiods = numberof_paymentperiods(creditterm)
    capitalinstallment = round(creditamount/numberofpaymentperiods,2)

    print()

    credittable = []
    headers = ["Period", "Credit Amount", "Interest","Total Installment"]
    credittable.append(headers)
    
    for i in range(numberofpaymentperiods):
        interest = round(creditamount * monthlyinterestrateonthecredit, 2)
        ratacalkowita = capitalinstallment + interest

        row = [i + 1, f"{creditamount:.2f}", f"{interest:.2f}", f"{ratacalkowita:.2f}"] 
        credittable.append(row)

        creditamount -= capitalinstallment

    tableready = tabulate.tabulate(credittable,headers="firstrow",tablefmt="pipe", colalign=('center', 'center', 'center', 'center')) 

    print(tableready)
      
    print()
    
    questionsaveinpdf= input("If you want to save the credit repayment schedule to a PDF file on your desktop, enter (y/yes), or press anything else to exit: ")

    if questionsaveinpdf.strip() in ["yes", "y"]:

        class PDF(FPDF):
            def header(self):
                # Ustawienie czcionki i nagłówków
                self.set_font('Courier', 'B', size=14)
                self.cell(w=30, h=10, text=headers[0], border=1, new_x='RIGHT', new_y='TOP', align="C")
                for header in headers[1:]:
                    self.cell(w=53, h=10, text=header, border=1, new_x='RIGHT', new_y='TOP', align="C")
                self.ln()  # Przejście do nowej linii po nagłówku

        #pdf.header() klasa zdefiniowana przed funkcją .add_page()
        #This method is used to render the page header. 
        #It is automatically called by add_page and should not be called directly by the application. 
        #The implementation in FPDF is empty, so you have to subclass it and override the method if you want a specific processing.
        
        pdf = PDF()
        pdf.set_auto_page_break(auto=True, margin=10)
        #auto=True: Włącza automatyczne dodawanie nowej strony, kiedy kończy się miejsce na bieżącej stronie. margin margines dolny równy 10
        pdf.add_page()

        pdf.set_font('Courier', '', 12)
        for line in credittable[1:]:
        # od 1, czyli drugiego elementu listy credittable
            for i, item in enumerate(line):
                if i == 0:
                    pdf.cell(w=30,h = 10, text=str(item),border=1, new_x='RIGHT', new_y='TOP', align="C")
                    # line[i] to item używając line[i] wyrzuca typeerror
                    #używając enumerate(line) mogę wskazać na kolejność numer i oraz konkretną pozycję, i komórki nie rozjeżdżają się na długość
                    #bo mam oddzielnie i jako numer oraz item jako zawartość listy line
                else:
                    pdf.cell(w=53,h=10, text=str(item), border =1, new_x='RIGHT', new_y='TOP', align="C")
                    #musiałem str - zmaienić liczbę na string, aby pdf.cell nie wyrzucał problemu
                
            pdf.ln()

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        # os.path.expanduser("~") zwróci C:\Users\NazwaUżytkownika lub /home/NazwaUżytkownika i join doda do tego Desktop
        # ~ atrybut do reprezentowania katalogu domowego
        pdf_path = os.path.join(desktop, "creditschedule.pdf")
        # zwróci C:\Users\Jan\Desktop\project.pdf utworzy/nadpisze ścieżkę
        # w pdf.output można skopiować ścieżkę na pulpit, ale metoda z biblioteką os bardziej bezpieczna
  
        pdf.output(pdf_path) 
        #pdf.output("project.pdf") 
        print(f"A PDF file with the credit repayment schedule has been saved on Desktop as: creditschedule.pdf")
    else:
        print("The option to create a PDF with the credit repayment schedule was not selected.")


# Tworzenie wielowierszowego ciągu tekstowego za pomocą return """ tekst """ albo note = """ tekst """ return note
def introductioninformation(): 
    return """
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    
    Welcome to the credit calculator with a fixed capital installment and decreasing credit installments.
    You will be asked for certain financial data in order to create a credit repayment schedule.
    You can enter the credit amount with a comma, e.g. 100,000 or as a single number without spaces.
    Enter the annual interest rate with or without the percentage sign, e.g. 10%, 10.75, 10 percent, 10percent.
    For the credit term, you can enter it as:
    - a number of payment periods
    - a number of months, e.g., 12 months, 12months, 12m, or 12 m
    - a number of years and months, e.g., 1 year 2 months; 1year2month; 1 y 2 m; 1y,2m
      (Remember: Instead of 12months, add 1 to the number of years)  

    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

def correct_creditamount():
    while True:
        amount = (input("Credit Amount: ")).strip()
        if re.search(r"^[1-9](\d{0,2}(,\d{3})*|\d*)$",amount):
            return int(amount.replace(",",""))
        #cyfry w grupach po trzy, oddzielone przecinkiem (\d{0,2}(,\d{3})*), lub
        #dodatkowe cyfry bez przecinków |\d*, co pozwala na liczby bez przecinków.
        else:
            print("Enter the credit amount in the correct format")
            continue              

def correct_annualinterestrate():
    while True:
        annualinterestrate = input("Annual Interest Rate: ").strip()             
        if re.search(r"^(\d|[1-9]\d+)(\.\d{1,2})?( ?%| ?percents?)?$", annualinterestrate): 
        #tutaj zmieniłem i dodałem błąd percents
            annualinterestrate = re.sub(r"( ?%| ?percents?)","", annualinterestrate)
            return float(annualinterestrate)
        else:
            print("Please enter the annual interest rate in the correct format")
            continue

def calculatethemonthlyinterestrate(annualinterestrateonthecredit):
    monthlyinterestrate = annualinterestrateonthecredit/100/12
    return monthlyinterestrate

def correct_creditterm(): 
 
    years = 0
    months = 0
    
    while True:
        creditterm = input("Credit Term: ").strip() 

        
        if matches:= re.search(r"^([1-9]\d*)$",creditterm, re.IGNORECASE):
            #print(matches.group(1))
            months = matches.group(1)

        elif matches := re.search(r"^(?P<months>1[0-2]|[1-9]) ?(m(onths?)?)$",creditterm, re.IGNORECASE):
            #tutaj przynajmniej musi być m po liczbie
            #print(matches.groups())
            months = matches.group(1)

        elif matches:= re.search(r"^(?P<years>[1-9]\d*)( ?(y(ears?)?)?)(( |, ?)(?P<months>1[0-1]|[1-9]) ?(m(onths?)?)?)?$",creditterm,re.IGNORECASE):
            # przerwa pomiędzy brak ? po ( |, ?)? i wtedy działa, blokuje 13months, bo wtedy nie zczytuje 13months do tego pattern
            #print(matches.groups())
            years = matches.group("years")

            if matches.group("months") is not None:
                months = matches.group("months")
            #print(years, months)

        else:
            print("Wprowadź poprawny format okresu kredytowania")
            continue

        return [int(years),int(months)]
          

def numberof_paymentperiods(creditterm):
    return creditterm[0]*12 + creditterm[1]

        
if __name__ == "__main__":
    main()

