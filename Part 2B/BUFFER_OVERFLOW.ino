

void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);        
}


void loop() {
  // put your main code here, to run repeatedly:
  byte data = 0;
  unsigned int ByteCount = 0;

  while(1)
  {
    data = 0;
    ByteCount = 0;
    while(ByteCount < 4000)
    {
      Serial.write(data);
      ByteCount ++;
      data++;
    }
    delay(1000);
  }
}
