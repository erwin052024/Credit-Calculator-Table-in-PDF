
import pytest
from unittest.mock import patch
from project import (correct_creditamount,
    correct_annualinterestrate,
    calculatethemonthlyinterestrate,
    correct_creditterm,
    numberof_paymentperiods,
    introductioninformation
)

# Testy poprawnie_kwotakredytu
@patch('builtins.input', side_effect=["-100", "abc", "1000", "1,000"])
def test_correct_creditamount(mock_input):
    assert correct_creditamount() == 1000  # poprawny format
    assert correct_creditamount() == 1000  # poprawny format z przecinkiem

    #mock_input jest automatycznie przekazywane do funkcji test_poprawnie_kwotakredytu jako argument przez dekorator @patch
    #W pytest możemy wykorzystać @patch z side_effect, by przekazać różne wartości do input. 
    #Funkcja przejdzie przez każde z tych wejść w kolejnych wywołaniach input, aż do momentu spełnienia warunku regularnego wyrażenia
    # mock_input Jest to obiekt mock przekazany do funkcji testującej test_poprawnie_kwotakredytu jako parametr
    #unittest.mock.patch(target, new=DEFAULT, spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs)
    #target musi być pełną ścieżką do obiektu, którą zaczyna się od modułu bazowego, np. 'builtins.input', by podmienić wbudowaną funkcję input
    #**kwargs Słownik dodatkowych argumentów przekazywanych do funkcji tworzącej mock, którymi mogą być np. specyficzne konfiguracje dla instancji mocka (np. return_value albo side_effect).
    #każdorazowe wywołanie input() podczas testu zwraca kolejną wartość z listy

# Test poprawnie_rocznastopaoprocentowania
@patch('builtins.input', side_effect=[ "abc", "-5%","10%", "15 percents"])
def test_correct_annualinterestrate(mock_input):
    assert correct_annualinterestrate() == 10
    assert correct_annualinterestrate() == 15


# Test liczmiesięczneoprocentowaniekredytu
def test_calculatethemonthlyinterestrate():
    assert calculatethemonthlyinterestrate(12) == pytest.approx(0.01, 0.001)
    assert calculatethemonthlyinterestrate(15) == pytest.approx(0.0125, 0.0001)

    #wynik testu będzie uznany za poprawny, jeżeli wartość testowana (np. wynik funkcji) mieści się w zakresie od 0.009 do 0.011 
    #(czyli ±0.001 wokół wartości 0.01)


# Test poprawnie_okres_kredytowania
@patch('builtins.input', side_effect=["13months", "5years", "10months", "2years, 6months"])
def test_correct_creditterm(mock_input):
    assert correct_creditterm() == [5, 0]
    assert correct_creditterm() == [0, 10]
    assert correct_creditterm() == [2, 6]



# Test liczbaokresówkredytowania
def test_lnumberof_paymentperiods():
    assert numberof_paymentperiods([1, 3]) == 15  # 1 rok i 3 miesiące
    assert numberof_paymentperiods([0, 12]) == 12  # tylko miesiące
    assert numberof_paymentperiods([2, 0]) == 24  # tylko lata


# Test introductioninformation
def test_introductioninformation():
    information = introductioninformation()
    assert "credit repayment schedule" in information
    assert "credit amount" in information 

    #Funkcja introductioninformation jest wywoływana i przypisana do zmiennej info, 
    #co pozwala przetestować jej wynik bez konieczności ponownego wywoływania funkcji.
    #sprawdza dokładnie nawet uwzględniając wielkość liter

