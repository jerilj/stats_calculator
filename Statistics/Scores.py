from CSVReader.TableReader import TableReader


def get_t_score(d, cl):
    table = TableReader('csv/t-table.csv')
    cl_i = None
    new_row = None

    for i, row in enumerate(table.data):
        if float(row[0]) >= d:
            if i != 0:
                prev = table.data[i - 1][0]
                p_diff = abs(float(prev) - float(d))
                c_diff = abs(float(row[0]) - float(d))
                if p_diff < c_diff:
                    new_row = table.data[i - 1]
                else:
                    new_row = row
                break

    for i, e in enumerate(table.header[1:len(table.header)]):
        if float(e) < cl:
            if i != 0:
                prev = table.header[i - 1]
                p_diff = abs(float(prev) - float(cl))
                c_diff = abs(float(e) - float(cl))
                if p_diff < c_diff:
                    cl_i = i - 1
                else:
                    cl_i = i
                break
        if float(e) == cl:
            cl_i = i
            break

    return new_row[cl_i + 1]


def get_z_score(d):
    score = None
    header_i = None
    table = TableReader('csv/z-table.csv')
    for idx, row in enumerate(table.data):
        for i, e in enumerate(row[1:len(row)]):
            if float(e) >= d and not score:
                if i != 0:
                    nxt = row[i + 1]
                    n_diff = abs(float(nxt) - float(d))
                    c_diff = abs(float(e) - float(d))
                    if n_diff > c_diff:
                        score = table.data[i - 1][0]
                        header_i = i - 1
                    else:
                        score = row[0]
                        header_i = i
            if float(e) == d and not score:
                score = row[0]
                header_i = i
    return float(score) + float(table.header[header_i + 1])
