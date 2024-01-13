import matplotlib
gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
for gui in gui_env:
    try:
        print("testing", gui)
        matplotlib.use(gui,warn=False, force=True)
        from matplotlib import pyplot as plt
        break
    except:
        continue
print("Using:",matplotlib.get_backend())
'''
credits : https://stackoverflow.com/questions/3285193/how-to-change-matplotlib-backends/43015816#43015816
for further clarification visit : https://stackoverflow.com/questions/73018899/how-to-fix-the-the-following-error-backend-tkagg-is-interactive-backend-turnin
'''
