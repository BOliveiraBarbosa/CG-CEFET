from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys

def calculaNormalFace(a, b, c):
    x = 0
    y = 1
    z = 2
    v0 = a
    v1 = b
    v2 = c
    U = (v2[x] - v0[x], v2[y] - v0[y], v2[z] - v0[z])
    V = (v1[x ] -v0[x], v1[y] - v0[y], v1[z] - v0[z])
    N = ((U[y] * V[z] - U[z] * V[y]), (U[z] * V[x] - U[x] * V[z]), (U[x] * V[y] - U[y] * V[x]))
    NLength = sqrt(N[x] * N[x] + N[y] * N[y] + N[z] * N[z])
    return (N[x] / NLength, N[y] / NLength, N[z] / NLength)

def draw():
	glPushMatrix()
	glTranslatef(0, -2, 0)
	glRotatef(-110, 1.0, 0.0, 0.0)

	raio = 2
	n = 4   # Quntidade de lados da base
	h = 5     # Altura

	base_superior = []
	base_inferior = []

	# base_superior
	glBegin(GL_POLYGON)
	for i in range(0, n):
		a = (i/n) * 2 * pi
		x = raio * cos(a)
		y = raio * sin(a)
		base_superior += [(x,y)]

		glVertex3f(x, y, h)
	glEnd()
	
	# base_inferior
	glBegin(GL_POLYGON)
	for i in range(0, n):
		a = (i/n) * 2 * pi
		x = raio * cos(a)
		y = raio * sin(a)
		base_inferior += [(x,y)]

		glVertex3f(x, y, 0.0)
	glEnd()

	glBegin(GL_QUADS)
	for i in range(0, n):
		glNormal3fv(calculaNormalFace((base_inferior[i][0], base_inferior[i][1], 0.0),
									  (-raio, -raio, h),
									  (base_inferior[(i+1) % n][0], base_inferior[(i+1) % n][1], 0.0)))
									  
		glVertex3f(base_inferior[i][0], base_inferior[i][1], 0.0)
		glVertex3f(base_superior[i][0], base_superior[i][1], h)

		glVertex3f(base_superior[(i+1) % n][0], base_superior[(i+1) % n][1], h)
		glVertex3f(base_inferior[(i+1) % n][0], base_inferior[(i+1) % n][1], 0.0)
		
	glEnd()

	glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    draw()
    glutSwapBuffers()

def reshape(w,h):
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	gluPerspective(45,float(w)/float(h),0.1,50.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	# Camera Virtual
	gluLookAt(10,0,0,0,0,0,0,1,0)

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)

def init():
	mat_ambient = (0.4, 0.0, 0.0, 1.0)
	mat_diffuse = (1.0, 0.0, 0.0, 1.0)
	mat_specular = (1.0, 0.5, 0.5, 1.0)
	mat_shininess = (50,)
	light_position = (10, 0, 0)
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_FLAT)

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_MULTISAMPLE)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow("LUZ")
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutTimerFunc(50,timer,1)
	init()
	glutMainLoop()

main()
