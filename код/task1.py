#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    school = {
        '1а': 23,
        '1б': 25,
        '2б': 24,
        '6а': 32,
        '7в': 22
    }

    # а) изменилось количество учащихся в одном из классов
    school['1а'] = 26

    # б) появился новый класс
    school['8г'] = 18

    # в) расформирован (удален) другой класс
    del school['2б']

    total_students = sum(school.values())
    print("Общее количество учащихся в школе:", total_students)
