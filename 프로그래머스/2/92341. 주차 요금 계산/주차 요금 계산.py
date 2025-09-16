import math

def solution(fees, records):
    parking_in = {}
    total_time = {}
    
    for record in records:
        time, car_num, state = record.split(' ')
        time_list = time.split(':')
        total_minutes = int(time_list[0]) * 60 + int(time_list[1])
        
        if state == 'IN':
            parking_in[car_num] = total_minutes
            
        else:
            in_time = parking_in[car_num]
            parking_time = total_minutes - in_time
            
            # 하루에 여러번 출차할 수도 있으니까.. 처음 출차시에만 0으로 초기화
            if car_num not in total_time:
                total_time[car_num] = 0
            total_time[car_num] += parking_time
            
            del parking_in[car_num]
    
    for car_num, in_time in parking_in.items():
        end_day = 23 * 60 + 59
        parking_time = end_day - in_time
        
        if car_num not in total_time:
            total_time[car_num] = 0
        total_time[car_num] += parking_time
        
    base_time, base_fee, unit_time, unit_fee = fees
    final_fees = {}
    
    for car_num, parking_time in total_time.items():
        if parking_time <= base_time:
            fee = base_fee
        else:
            extra_time = parking_time - base_time
            extra_unit_time = math.ceil(extra_time / unit_time)
            fee = base_fee + extra_unit_time * unit_fee
        
        final_fees[car_num] = fee
        
    sorted_cars = sorted(final_fees.keys())
    result = [final_fees[car] for car in sorted_cars]
    
    return result