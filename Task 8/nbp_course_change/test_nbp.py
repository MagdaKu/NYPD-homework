import nbp_change

mock_response = {
        "chf": ([4.55, 4.52, 4.52], "frank szwajcarski"),
        "usd": ([3.43, 3.52, 3.55], "dolar amerykański"),
        "gbp": ([5.0231, 5.0283, 5.0141, 5.0144, 5.0319], "funt szterling")
    }

def mock_get(currency_code, days):
    full_data = mock_response[currency_code]
    values = full_data[0][-days:]  #upewniam się że bierze dobrą liczbę ostatnich dni
    full_name = full_data[1] #nazwa waluty
    return values, full_name 

def test_calc_statistics(monkeypatch):
    monkeypatch.setattr("nbp_change.get_courses", mock_get)
    res = {}
    currency_list = ["chf", "usd", "gbp"]
    days = [3,3,5]
    for i in range(len(currency_list)):
        values, full_name = nbp_change.get_courses(currency_list[i], days[i])
        change = values[-1] / values[0]
        res[currency_list[i]] = {
            "change": change,
            "course": values[-1],
            "full_name": full_name,
        }
 
    assert res["chf"] == {
    "change": 4.52 / 4.55, #values[-1] / values[0]
    "course": 4.52,
    "full_name": "frank szwajcarski"}

    assert res["usd"] == {
        "change": 3.55 / 3.43,
        "course": 3.55,
        "full_name": "dolar amerykański"
    }
    assert res["gbp"] == {
        "change": 5.0319 / 5.0231, 
        "course": 5.0319,
        "full_name": "funt szterling"
    }