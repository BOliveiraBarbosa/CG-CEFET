float r = 0;
float theta = 0;

void setup()
{
  size(800,800);
  background(0);
}

void draw()
{
   translate(width/2, height/2);
   noStroke();
   fill(135,206,235);
   
  float x = r * cos(theta); //cos(theta) = CA/H
  float y = r * sin(theta); //sen(theta) = CO/H
  
  if(r < 400)
  {
    ellipse(x, y, 10, 10);
  }  
  
  theta += 0.01;
  r += 0.1;
}
