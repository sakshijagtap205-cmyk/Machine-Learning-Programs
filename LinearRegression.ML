import java.util.*;

public class LinearRegressionML {

    static double m = 0;
    static double b = 0;
    static double learningRate = 0.0001;

    static void train(double[] x, double[] y, int epochs) {

        int n = x.length;

        for (int epoch = 0; epoch < epochs; epoch++) {

            double dm = 0;
            double db = 0;

            for (int i = 0; i < n; i++) {

                double prediction = m * x[i] + b;
                double error = prediction - y[i];

                dm += error * x[i];
                db += error;
            }

            m -= learningRate * (2.0 / n) * dm;
            b -= learningRate * (2.0 / n) * db;

            if (epoch % 1000 == 0) {
                System.out.println(
                    "Epoch: " + epoch +
                    " | m = " + m +
                    " | b = " + b
                );
            }
        }
    }

    static double predict(double x) {
        return m * x + b;
    }

    public static void main(String[] args) {

        double[] hours = {
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10
        };

        double[] marks = {
            35, 40, 45, 50, 55,
            60, 65, 70, 75, 80
        };

        train(hours, marks, 10000);

        double studyHours = 7.5;
        double prediction = predict(studyHours);

        System.out.println("\nML Model Trained");
        System.out.println("Slope: " + m);
        System.out.println("Intercept: " + b);
        System.out.println(
            "Predicted Marks for " +
            studyHours + " hours = " + prediction
        );
    }
}