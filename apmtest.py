import sys, time, random
from ddtrace import tracer

@tracer.wrap(name='web.user.home', service='webapp')
def Test_Function_A(Parm_A):
        span = tracer.current_span()
        span.set_tag('Parm_Tag_A', Parm_A)
        output_str = 'Testing, %s!' % Parm_A
        randomnum = random.randint(1,31)
        time.sleep(randomnum)
        print(output_str)

@tracer.wrap(name='db.query', service='database')
def Test_Function_B(Parm_B):
        span = tracer.current_span()
        span.set_tag('Parm_Tag_B', Parm_B)
        output_str = 'Testing, %s!' % Parm_B
        randomnum = random.randint(1,21)
        time.sleep(randomnum)
        print(output_str)


assert len(sys.argv) == 2

Parm_A = sys.argv[1]
Test_Function_A(Parm_A)
time.sleep(1)

Parm_B = sys.argv[1]
Test_Function_B(Parm_B)
time.sleep(1)
