from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from math import*

def parabola():
    glRotatef(1, 0, 1, 0)
    glBegin(GL_POINTS)

    raio_i = -2
    raio_f = 2
    n = 50

    for i in range(0, n):
        for j in range(0, n):

            raio = i * (raio_f - raio_i)/n + raio_i
            theta = (j * pi)/n

            x = raio * cos(theta)
            y = pow(raio,2)
            z = raio * sin(theta)

            glVertex3f(x, y, z)
    glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    parabola()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

#Programa Principal
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Parábola")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0/600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)
glutTimerFunc(50, timer, 1)
glutMainLoop()
