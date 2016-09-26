import java.awt.Color;
import java.awt.Graphics;
import java.util.Scanner;

public class Test {
    public static void main (String[] args) {
        int S = 500;

        DrawingPanel d = new DrawingPanel(S, S);
        Graphics g = d.getGraphics();

        drawInfinity(g, S, 10);
    }

    public static void drawInfinity(Graphics g, int s, int n) {
        g.setColor(Color.BLACK);

        double xs = s / 2.0;

        int x = (int) ((xs - Math.sqrt(xs)) / 2.0);
        g.fillRect(x, x, (int) xs, (int) xs);

        for (int i = 1; i <= n; ++i) {
            double dx = Math.sqrt(xs) / 2.0;
            double nx = xs / 2.0;

            int x = (int) (nx - dx);
            int ns = (int) xs;

            if (i % 2 == 1) {
                g.fillRect(x, x, ns, ns);
                g.fillRect(x, s - x - ns, ns, ns);
            }
            else {
                g.drawRect(x, x, ns, ns);
                g.drawRect(x, s - x - ns, ns, ns);
            }

            xs /= 2.0;
        }
    }
}
