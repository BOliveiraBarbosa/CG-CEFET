from statistics import quantiles
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math

cores = (
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 1, 1),
    (0, 0, 1),
    (1, 0, 1),
    (0.5, 1, 1),
    (1, 0, 0.5),
)

quadro = 0

def desenha():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(quadro, 0.0, 1.0, 0.0)
    glRotatef(90.0 + quadro, 1.0, 0.0, 0.0)

    raio = 0.7
    n = 6 # Quntidade de lados da base
    h = 1   # Altura

    #Lados
    glBegin(GL_TRIANGLES)

    for i in range(0, n):
        glColor3fv(cores[(i) % len(cores)])
        glVertex3f(0.0, 0.0, -1.0)

        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        z = h
        glVertex3f(x, y, z)

        a = ((i+1)/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x, y, z)

    glEnd()

    # Fundo
    glBegin(GL_TRIANGLE_FAN)

    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(0.0, 0.0, 0.0)

    for i in range(0, n+1):

        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x, y, z)

    glEnd()

    glutSwapBuffers()
    quadro += 1

    glPopMatrix()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)

# Programa Principal
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Piramide")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0/600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -5.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
