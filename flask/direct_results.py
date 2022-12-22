from flask import render_template

# vit, prot, fib, carb = "+15", "+32", "+20", "-10"
def get_diet(pred, name, prob):
    msg = ['So, ', 'you control your diabetes']
    walk = 7
    pr = int(prob[0][1] * 100)
    if pred == 1:
        if 50 <= pr and pr <= 60:
            vit, prot, fib, carb = "+15", "+32", "+20", "-10"
        elif pr <= 80:
            vit, prot, fib, carb = "+25", "+37", "+40", "-60"
        else:
            vit, prot, fib, carb = "+30", "+40", "60", "-90"
    else:
        msg = ["That's great!!! You are at a low risk of having diabetes. And ", "maintain your good health."]
        walk = 4
        vit, prot, fib, carb = "+05", "+05", "+06", "-03"
    print(vit, prot, fib, carb)
    # return render_template('test01.html', name=name, vitamin=vit, percent=pr, prot=prot, fib=fib, carb=carb)
    return render_template('results.html', name=name, vitamin=vit, percent=pr, prot=prot, fib=fib, carb=carb, msg=msg,
                           walk=walk)
