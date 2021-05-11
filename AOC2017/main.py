if __name__ == '__main__':
    for i in range(25):
        exec('from day{:02d} import solve{:02d}'.format(i+1, i+1))
        print('----- day '+str(i+1)+' ----')
        exec('solve{:02d}()'.format(i+1))
