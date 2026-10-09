# app.py

from flask import Flask, render_template, request
from models import calculate_iis_ilm_equilibrium

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # المسار الرئيسي للوحة تحكم IIS-ILM
    equilibrium_result = None
    
    if request.method == 'POST':
        try:
            # استخراج المتغيرات من واجهة المستخدم
            alpha = float(request.form.get('alpha', 0.15))
            psi = float(request.form.get('psi', 0.5))
            I0 = float(request.form.get('I0', 1200))
            C0 = float(request.form.get('C0', 400))
            Z = float(request.form.get('Z', 250))
            D = float(request.form.get('D', 100))
            beta = float(request.form.get('beta', 0.3))
            d = float(request.form.get('d', 0.6))
            phi0 = float(request.form.get('phi0', 300))
            M_OF = float(request.form.get('M_OF', 2200))
            
            # تنفيذ دالة النمذجة الرياضية
            equilibrium_result = calculate_iis_ilm_equilibrium(
                alpha, psi, I0, C0, Z, D, beta, d, phi0, M_OF
            )
        except ValueError:
            pass
            
    return render_template('index.html', result=equilibrium_result)

if __name__ == '__main__':
    # تشغيل الخادم على المنفذ 5001 لتفادي التعارض مع المشروع الأول
    app.run(debug=True, port=5001)