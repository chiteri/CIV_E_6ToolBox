def earthwork_volume (current_cross_section_area, previous_cross_section_area, station_length):
    average_end_area = (current_cross_section_area + previous_cross_section_area) / 2
    volume_cubic_feet = average_end_area * station_length
    SQUARE_FEET_TO_CUBIC_FEET = (3*3*3) # Volume in cubic yard, divide by a factor of 27
    return volume_cubic_feet / SQUARE_FEET_TO_CUBIC_FEET 
