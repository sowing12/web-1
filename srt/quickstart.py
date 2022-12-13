'''
pip install -r requirements.txt
python quickstart.py --user 1581387959 --psw ohoh5665!@  --dpt 나주 --arr 수서 --dt 20221004 --tm 08
'''

# imports
from srt_reservation.main import SRT
from srt_reservation.util import parse_cli_args


if __name__ == "__main__":
    cli_args = parse_cli_args()

    
    login_id = "1581387959"
    login_psw = "ohoh5665!@"
    dpt_stn = "나주"
    arr_stn = "수서"
    dpt_dt = "20221216"
    dpt_tm = "08"
    
    
    num_trains_to_check = 2
    want_reserve = 1

    srt = SRT(dpt_stn, arr_stn, dpt_dt, dpt_tm, num_trains_to_check, want_reserve)
    srt.run(login_id, login_psw)
