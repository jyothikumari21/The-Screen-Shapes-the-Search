from io import BytesIO
import pandas as pd
from src.analysis import position_summary, session_clicks
from src.data import parse_csv

def test_position_summary_all_six():
    d = pd.DataFrame({'location':[1,1,6]})
    res = position_summary(d)
    assert res.clicks.tolist() == [2,0,0,0,0,1]
    assert round(res.share_pct.sum(),6) == 100.0

def test_session_sorted():
    d = pd.DataFrame({'session_id':[7,7,8],'order':[2,1,1]})
    assert session_clicks(d,7)['order'].tolist() == [1,2]

def test_parse_csv():
    fields = ['2008','4','1','1','29','18817','1','A1','1','6','1','33','1','1']
    header = ';'.join('x'+str(i) for i in range(14))
    df = parse_csv((header+'\n'+';'.join(fields)+'\n').encode())
    assert df.loc[0,'position_name'] == 'Bottom right'
