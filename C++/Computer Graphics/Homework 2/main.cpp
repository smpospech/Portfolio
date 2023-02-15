/*******************************************************
 * Homework 2: OpenGL                                  *
 *-----------------------------------------------------*
 * First, you should fill in problem1(), problem2(),   *
 * and problem3() as instructed in the written part of *
 * the problem set.  Then, express your creativity     *
 * with problem4()!                                    *
 *                                                     *
 * Note: you will only need to add/modify code where   *
 * it says "TODO".                                     *
 *                                                     *
 * The left mouse button rotates, the right mouse      *
 * button zooms, and the keyboard controls which       *
 * problem to display.                                 *
 *                                                     *
 * For Linux/OS X:                                     *
 * To compile your program, just type "make" at the    *
 * command line.  Typing "make clean" will remove all  *
 * computer-generated files.  Run by typing "./hw2"    *
 *                                                     *
 * For Visual Studio:                                  *
 * You can create a project with this main.cpp and     *
 * build and run the executable as you normally would. *
 *******************************************************/

#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#include "./freeglut-3.2.1/include/GL/freeglut.h"

using namespace std;

bool leftDown = false, rightDown = false;
int lastPos[2];
float cameraPos[4] = {0,1,4,1};
int windowWidth = 640, windowHeight = 480;
double yRot = 0;
int curProblem = 4; // TODO: change this number to try different examples

float specular[] = { 1.0, 1.0, 1.0, 1.0 };
float shininess[] = { 50.0 };

void problem1() { //teapot circle
  //gluSolidTeapot(), gluSolidCUbe(), glPushMatrix(), glPopMatrix(), glTranslatef(), glScalef(), glRotatef()
  glMatrixMode(GL_MODELVIEW);
  
  double teapotSize = 0.1;
  double radius = 1.2;
  double radians = 0;
  double pi = 3.14159265359;

  for(int i=0; i<10; i++){
    glPushMatrix();
    radians = ((i*36) * pi)/180;
    glTranslatef((radius * sin(radians)), (radius * cos(radians)), 0);
    glRotatef((90-(i*36)), 0, 0, 1);
    glutSolidTeapot(teapotSize);
    glPopMatrix();
    }
  glFlush();
}

void problem2() { //staircase
  glMatrixMode(GL_MODELVIEW);

  glPushMatrix(); //9
  glTranslatef(1.62,0.03,0);
  glScalef(0.15,0.30,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //8
  glTranslatef(1.44,0.06,0);
  glScalef(0.15,0.35,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //7
  glTranslatef(1.26,0.09,0);
  glScalef(0.15,0.40,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //6
  glTranslatef(1.08,0.12,0);
  glScalef(0.15,0.45,0);
  glutSolidCube(1.25);
  glPopMatrix();
  
  glPushMatrix(); //5
  glTranslatef(0.9,0.15,0);
  glScalef(0.15,0.50,0);
  glutSolidCube(1.25);
  glPopMatrix();
  
  glPushMatrix(); //4
  glTranslatef(0.72,0.18,0);
  glScalef(0.15,0.55,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //3
  glTranslatef(0.54,0.21,0);
  glScalef(0.15,0.60,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //2
  glTranslatef(0.36,0.24,0);
  glScalef(0.15,0.65,0);
  glutSolidCube(1.25);
  glPopMatrix();
  
  glPushMatrix(); //1
  glTranslatef(0.18,0.27,0);
  glScalef(0.15,0.70,0);
  glutSolidCube(1.25);
  glPopMatrix();
  
  glPushMatrix(); //og
  glTranslatef(0,0.3,0);
  glScalef(0.15,0.75,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //-1
  glTranslatef(-0.18,0.33,0);
  glScalef(0.15,0.80,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //-2
  glTranslatef(-0.36,0.37,0);
  glScalef(0.15,0.85,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //-3
  glTranslatef(-0.54,0.4,0);
  glScalef(0.15,0.90,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //-4
  glTranslatef(-0.72,0.43,0);
  glScalef(0.15,0.95,0);
  glutSolidCube(1.25);
  glPopMatrix(); 

  glPushMatrix(); //-5
  glTranslatef(-0.90,0.46,0);
  glScalef(0.15,1,0);
  glutSolidCube(1.25);
  glPopMatrix(); 

  glPushMatrix(); //-6
  glTranslatef(-1.08,0.49,0);
  glScalef(0.15,1.05,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glPushMatrix(); //-7
  glTranslatef(-1.26,0.52,0);
  glScalef(0.15,1.10,0);
  glutSolidCube(1.25);
  glPopMatrix(); 

  glPushMatrix(); //-8
  glTranslatef(-1.44,0.55,0);
  glScalef(0.15,1.15,0);
  glutSolidCube(1.25);
  glPopMatrix(); 

  glPushMatrix(); //-9
  glTranslatef(-1.62,0.58,0);
  glScalef(0.15,1.20,0);
  glutSolidCube(1.25);
  glPopMatrix(); 

  glPushMatrix(); //-10
  glTranslatef(-1.80,0.61,0);
  glScalef(0.15,1.25,0);
  glutSolidCube(1.25);
  glPopMatrix(); 

  glPushMatrix(); //magic line
  glTranslatef(-0.1,-0.15,0);
  glScalef(2.9,0.1,0);
  glutSolidCube(1.25);
  glPopMatrix();

  glFlush();

  
  /*double tick = .61;
  double scalefactor = 3.5;
  
  for(int i=0; i<10; i++){
    for(double j=-1.8; j<0;){
      glPushMatrix(); //4
      glTranslatef(j,tick,0);
      glScalef(0.15,scalefactor,0);
      glutSolidCube(1.25);
      glPopMatrix();
      j += .18;
      tick -= 0.03;
      scalefactor -= 0.05;
    }
  }*/
  
}

void problem3() { // teapot pyramid
  glMatrixMode(GL_MODELVIEW); //21 teapots
  double teapotSize = 0.1;

  for(double i=-0.75; i<1;){ // row of 6
    glPushMatrix();
    glTranslatef(i,0.6,0);
    glutSolidTeapot(teapotSize);
    glPopMatrix();
    i += 0.3;
  }

  for(double i=-0.65; i<0.7;){ // row of 5
    glPushMatrix();
    glTranslatef(i,0.3,0);
    glutSolidTeapot(teapotSize);
    glPopMatrix();
    i += 0.3;
  }

  for(double i=-0.5; i<0.4;){ // row of 4
    glPushMatrix();
    glTranslatef(i,0,0);
    glutSolidTeapot(teapotSize);
    glPopMatrix();
    i += 0.3;
  }
  
  for(double i =-0.4; i<0.3;){ // row of 3
    glPushMatrix();
    glTranslatef(i,-0.3,0);
    glutSolidTeapot(teapotSize);
    glPopMatrix();
    i+= 0.3;
  }

  for(double i=-0.2; i<0.1;){ // row of 2
    glPushMatrix();
    glTranslatef(i,-0.6,0);
    glutSolidTeapot(teapotSize);
    glPopMatrix();
    i+= 0.3;
  }

  glPushMatrix(); // row of 1
  glTranslatef(-0.05,-0.9,0);
  glutSolidTeapot(teapotSize);
  glPopMatrix();

  glFlush();
  
  /*glPushMatrix();
  glTranslatef(-0.1,-0.3,0);
  glRotatef(0, 1, 0, 0);
  glutSolidTeapot(teapotSize);
  glPopMatrix();*/
  
}

void problem4() { //original picture 
  glShadeModel(GL_SMOOTH);
  glBegin(GL_TRIANGLES); //original triangle
    glColor3f(1,0,0);
    glVertex3f(-1,0,0); //left vertex

    glColor3f(0,1,0);
    glVertex3f(1,0,0); //right vertex
  
    glColor3f(0,0,1);
    glVertex3f(0,1,0); // upper vertex
  glEnd();

  glBegin(GL_TRIANGLES); //upper triangle
    glColor3f(1,0,0); //tip
    glVertex3f(0,1,0);

    glColor3f(0,1,0); 
    glVertex3f(0.3,1.3,0); //right vertex
  
    glColor3f(0,0,1);
    glVertex3f(-0.3,1.3,0); // left vertex
  glEnd();

  glBegin(GL_TRIANGLES); //left triangle
    glColor3f(1,0,0); //tip
    glVertex3f(-1,0,0);

    glColor3f(0,1,0); 
    glVertex3f(-1.3,0.3,0); //right vertex
  
    glColor3f(0,0,1);
    glVertex3f(-1.3,-0.3,0); // left vertex
  glEnd();

  glBegin(GL_TRIANGLES); //right triangle
    glColor3f(1,0,0); //tip
    glVertex3f(1,0,0);

    glColor3f(0,1,0); 
    glVertex3f(1.3,0.3,0); //right vertex
  
    glColor3f(0,0,1);
    glVertex3f(1.3,-0.3,0); // left vertex
  glEnd();

  double teapotSize = 0.08;

  glPushMatrix();
    glPushMatrix();
      glTranslatef(-1,0,0);
      glutSolidTeapot(teapotSize);
      glTranslatef(2,0,0);
      glutSolidTeapot(teapotSize);
    glPopMatrix();
    glTranslatef(0,1,0);
    glutSolidTeapot(teapotSize);
  glPopMatrix();

  glPushMatrix();
    glPushMatrix();
      glTranslatef(-1.3,0.3,0);
      glRotatef(90, 0, 0, 1);
      glutSolidTeapot(teapotSize);
      glTranslatef(0,-2.55,0);
      glutSolidTeapot(teapotSize);
    glPopMatrix();
    glTranslatef(-1.3,-0.3,0);
    glRotatef(90, 0, 0, 1);
    glutSolidTeapot(teapotSize);
    glTranslatef(0,-2.55,0);
    glutSolidTeapot(teapotSize);
  glPopMatrix();

  glPushMatrix();
    glTranslatef(-0.3,1.3,0);
    glRotatef(180, 0, 0, 1);
    glutSolidTeapot(teapotSize);
    glTranslatef(-0.6,0,0);
    glutSolidTeapot(teapotSize);
  glPopMatrix();
  
  glFlush();
  
}

void display() {
	glClearColor(0,0,0,0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glDisable(GL_LIGHTING);
	glEnable(GL_DEPTH_TEST);
	glBegin(GL_LINES);
		glColor3f(1,0,0); glVertex3f(0,0,0); glVertex3f(1,0,0); // x axis
		glColor3f(0,1,0); glVertex3f(0,0,0); glVertex3f(0,1,0); // y axis
		glColor3f(0,0,1); glVertex3f(0,0,0); glVertex3f(0,0,1); // z axis
	glEnd(/*GL_LINES*/);

	glEnable(GL_LIGHTING);
	glShadeModel(GL_SMOOTH);
	glMaterialfv(GL_FRONT, GL_SPECULAR, specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, shininess);
	glEnable(GL_LIGHT0);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glViewport(0,0,windowWidth,windowHeight);

	float ratio = (float)windowWidth / (float)windowHeight;
	gluPerspective(50, ratio, 1, 1000);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	gluLookAt(cameraPos[0], cameraPos[1], cameraPos[2], 0, 0, 0, 0, 1, 0);

	glLightfv(GL_LIGHT0, GL_POSITION, cameraPos);

	glRotatef(yRot,0,1,0);

	if (curProblem == 1) problem1();
	if (curProblem == 2) problem2();
	if (curProblem == 3) problem3();
	if (curProblem == 4) problem4();

	glutSwapBuffers();
}

void mouse(int button, int state, int x, int y) {
	if (button == GLUT_LEFT_BUTTON) leftDown = (state == GLUT_DOWN);
	else if (button == GLUT_RIGHT_BUTTON) rightDown = (state == GLUT_DOWN);

	lastPos[0] = x;
	lastPos[1] = y;
}

void mouseMoved(int x, int y) {
	if (leftDown) yRot += (x - lastPos[0])*.1;
	if (rightDown) {
		for (int i = 0; i < 3; i++)
			cameraPos[i] *= pow(1.1,(y-lastPos[1])*.1);
	}


	lastPos[0] = x;
	lastPos[1] = y;
	glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y) {
	curProblem = key-'0';
    if (key == 'q' || key == 'Q' || key == 27){
        exit(0);
    }
	glutPostRedisplay();
}

void reshape(int width, int height) {
	windowWidth = width;
	windowHeight = height;
	glutPostRedisplay();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(windowWidth, windowHeight);
	glutCreateWindow("HW2");

	glutDisplayFunc(display);
	glutMotionFunc(mouseMoved);
	glutMouseFunc(mouse);
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);

	glutMainLoop();

	return 0;
}
