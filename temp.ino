int temp;
float temperatura;
void setup()
{
  Serial.begin(9600); 
}

void loop()
{
  temp=analogRead(A0);
  temperatura=(5.0*temp*100.0)/1023.0;
  Serial.print("T= ");
  Serial.println(temperatura);
  delay(500);
}

