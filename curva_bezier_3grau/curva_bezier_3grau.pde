void setup()
{
  size(800, 800);
  stroke(0);
}

void draw()
{
  background(128);
  
  float P0X = 100;
  float P0Y = 350;
  
  float P1X = 100;
  float P1Y = 700;
  
  float P2X = mouseX;
  float P2Y = mouseY;
  
  float P3X = 700;
  float P3Y = 350;
  
  beginShape();
  vertex(P0X, P0Y);
  
  for(float t = 0; t <= 1; t +=0.01)
  {
    /* ~~ EIXO DAS ABSCISSAS ~~ */
    float AX = P0X + t * (P1X - P0X);
    float BX = P1X + t * (P2X - P1X);
    float CX = P2X + t * (P3X - P2X);
    
    float DX = AX + t * (BX - AX);
    float EX = BX + t * (CX - BX);
    
    float FX = DX + t * (EX - DX);
    
    /* ~~ EIXO DAS ORDENADAS ~~ */
    
    float AY = P0Y + t * (P1Y - P0Y);
    float BY = P1Y + t * (P2Y - P1Y);
    float CY = P2Y + t * (P3Y - P2Y);
    
    float DY = AY + t * (BY - AY);
    float EY = BY + t * (CY - BY);
    
    float FY = DY + t * (EY - DY);
    
    vertex(FX, FY);
  }
  vertex(P3X, P3Y);
  endShape(CLOSE);
}
