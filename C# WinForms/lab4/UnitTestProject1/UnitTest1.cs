using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using WindowsFormsApp1;
namespace UnitTestProject1
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            // Исходные данные для теста.
            Double[] myArray = { 2.4, -6.1, -3.9, 5.6 };

            // Ожидаемое значение (2.4 + 5.6)/2 = 4.0
            Double experted = 4.0;

            // Вызов тестируемой функции.
            Form1 form1 = new Form1();
            Double actual = form1.averagePositiv(myArray);

            Assert.AreEqual(experted, actual, 0.00, "Ожидаемое среднее арифметическое положительных элементов массива не было получено!");
        }

        [TestMethod]
        public void TestMethod2()
        {
            // Исходные данные для теста.
            Double[] myArray = { -1.2, -9.6, -11.5, -7.8 };


            // Вызов тестируемой функции.
            Form1 form1 = new Form1();
            try
            {
                Double actual = form1.averagePositiv(myArray);
            }
            catch (Exception ex)
            {
                // Содержит ли строка заданное сообщение.
                StringAssert.Contains(ex.Message, "В массиве нет положительных!");
                return;
            }
            Assert.Fail("Ожидаемое исключение не было получено.");
        }

    }
}
