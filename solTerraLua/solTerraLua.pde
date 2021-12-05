void setup()
{
  size(800,800);
}

void draw()
{
  background(0);
  noStroke();
  
  fill(255,255,0);
  translate(width/2, height/2);
  circle(0,0,150);
  
  
  fill(0,0,255);
  rotate(frameCount/(20*TWO_PI));
  translate(width/3,0);
  circle(0,0,50);
  
  
  fill(255);
  rotate(frameCount/(5*TWO_PI));
  circle(75,0,20);
}
