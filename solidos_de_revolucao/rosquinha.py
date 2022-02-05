from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from math import*

rotacao = 0

def rosquinha():
    #glTranslate(4,0,0)
    glRotatef(rotacao, 1, 1, 0)
    glBegin(GL_POINTS)

    raio_maior = 2
    raio_menor = 1
    n = 50

    for i in range(0, n):
        for j in range(0, n):

            theta = (i*2*pi)/n
            phi = (j*2*pi)/n

            x = (raio_maior + raio_menor * cos(theta)) * cos(phi)
            y = (raio_maior + raio_menor * cos(theta)) * sin(phi)
            z = raio_menor * sin(theta)

            glVertex3f(x, y, z)

    glEnd()

def desenha():
    global rotacao

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix() 
    rosquinha()
    glPopMatrix()

    glutSwapBuffers()

    rotacao += 1

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

#Programa Principal
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Rosquinha")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0/600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -15)
glutTimerFunc(50, timer, 1)
glutMainLoop()
