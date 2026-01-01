def f(subjecs):
    math_avg = sum(subjecs['math'])/len(subjecs['math'])
    geo_avg = sum(subjecs['geo'])/len(subjecs['geo'])
    comp_avg = sum(subjecs['comp'])/len(subjecs['comp'])
    table= [math_avg,geo_avg,comp_avg]
    if math_avg > geo_avg and math_avg >comp_avg:
        return "math"
    elif geo_avg > math_avg and geo_avg > comp_avg:
        return "geo"
    else:
        return "comp"
if __name__ == "__main__":
    print(f({"math":[3,4,4],'geo':[5,4,4,4],"comp":[5,4]}))