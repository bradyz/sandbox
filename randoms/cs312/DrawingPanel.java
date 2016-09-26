// DrawingPanel
// Derived from class by Stuart Reges and Marty Stepp
//                       07/01/2005

// This version has been hacked a bit by various CS 314 TAs.

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.image.BufferedImage;

import javax.imageio.ImageIO;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;
import javax.swing.WindowConstants;
import javax.swing.event.MouseInputAdapter;

/**
 * The DrawingPanel class provides a simple interface for drawing persistent
 * images using a Graphics object. An internal BufferedImage object is used to
 * keep track of what has been drawn. A client of the class simply constructs a
 * DrawingPanel of a particular size and then draws on it with the Graphics
 * object, setting the background color if they so choose. To ensure that the
 * image is always displayed, a timer calls repaint at regular intervals.
 */
public class DrawingPanel implements ActionListener {
    public static final int DELAY = 250; // delay between repaints in millis

    public static final String DUMP_IMAGE_PROPERTY_NAME = "drawingpanel.save";
    public static boolean dumpImage = false; // true to write DrawingPanel to file
    public static String saveImageFileName = null;
    public static boolean numberSavedFiles = false; // append numeric to name?

    protected static int saveFileNum = 0;

    private static final boolean PRETTY = true; // true to anti-alias

    protected int width, height; // dimensions of window frame
    protected JFrame frame; // overall window frame
    protected JPanel panel; // overall drawing surface
    protected BufferedImage image; // remembers drawing commands
    protected Graphics2D g2; // graphics context for painting
    protected JLabel statusBar; // status bar showing mouse position
    protected long createTime;
    protected Timer repaintTimer;


    static {
        saveImageFileName = System.getProperty(DUMP_IMAGE_PROPERTY_NAME);
        dumpImage = saveImageFileName != null;
    }

    /** Construct a drawing panel of given width and height enclosed in a window */
    public DrawingPanel(final int width, final int height) {
        this.width = width;
        this.height = height;
        image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

        statusBar = new JLabel(" ");
        statusBar.setBorder(BorderFactory.createLineBorder(Color.BLACK));

        panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 0));
        panel.setBackground(Color.WHITE);
        panel.setPreferredSize(new Dimension(width, height));
        panel.add(new JLabel(new ImageIcon(image)));

        /* listen to mouse movement */
        final MouseInputAdapter listener = new MouseInputAdapter() {
            @Override
            public void mouseMoved(final MouseEvent e) {
                statusBar.setText("(" + e.getX() + ", " + e.getY() + ")");
            }

            @Override
            public void mouseExited(final MouseEvent e) {
                statusBar.setText(" ");
            }
        };
        panel.addMouseListener(listener);
        panel.addMouseMotionListener(listener);

        g2 = (Graphics2D) image.getGraphics();
        g2.setColor(Color.BLACK);
        if (PRETTY) {
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2.setStroke(new BasicStroke(1.1f));
        }

        if (!java.awt.GraphicsEnvironment.isHeadless()) {
            frame = new JFrame("Drawing Panel");
        }
        if (frame != null) {
            frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
            frame.setResizable(false);
            frame.addWindowListener(new WindowAdapter() {
                @Override
                public void windowClosing(final WindowEvent e) {
                    handleWindowClosing();
                }
            });
            frame.getContentPane().add(panel);
            frame.getContentPane().add(statusBar, "South");
            frame.pack();
            frame.setVisible(true);
        }
        createTime = System.currentTimeMillis();
        if (dumpImage) {
            if (frame != null) {
                frame.toBack();
            }
        } else {
            toFront();
        }

        if (frame != null) {
            /* repaint timer so that the screen will update */
            repaintTimer = new Timer(DELAY, this);
            repaintTimer.start();
        } else {
            Thread saveThread = new Thread("DrawingPanel delayed save thread") {
                @Override
                public void run() {
                    try {
                        Thread.sleep(4 * DELAY);
                    } catch (InterruptedException e) {
                        // Just stop sleeping on interrupt
                    } finally {
                        handleWindowClosing();
                    }
                }
            };
            saveThread.start();
        }
    }

    /** Called by an internal timer that keeps repainting */
    @Override
    public void actionPerformed(final ActionEvent e) {
        panel.repaint();
        if (dumpImage && System.currentTimeMillis() > createTime + 4 * DELAY) {
            repaintTimer.stop();
            if (frame != null) {
                frame.dispatchEvent(new WindowEvent(frame, WindowEvent.WINDOW_CLOSING));
            }
        }
    }

    /** Do window close-time processing */
    protected void handleWindowClosing() {
        if (repaintTimer != null) {
            repaintTimer.stop();
        }
        if (frame != null) {
            frame.setVisible(false);
        }
        if (dumpImage) {
            String filename = saveImageFileName;
            if (numberSavedFiles) {
                int dot = filename.lastIndexOf('.');
                saveFileNum++;
                filename = filename.substring(0, dot) + saveFileNum + filename.substring(dot);
            }
            save(filename);
        }
        if (frame != null) {
            frame.dispose();
        }
    }

    /** Obtain the Graphics object to draw on the panel */
    public Graphics2D getGraphics() {
        return g2;
    }

    /** Set the background color of the drawing panel */
    public void setBackground(final Color c) {
        panel.setBackground(c);
    }

    /** Show or hide the drawing panel on the screen */
    public void setVisible(final boolean visible) {
        if (frame != null) {
            frame.setVisible(visible);
        }
    }

    /** Take the current contents of the panel and write them to a file */
    public void save(final String filename) {
        final String extension = filename.substring(filename.lastIndexOf(".") + 1);

        /* Create second image so we get the background color */
        final BufferedImage image2 = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        final Graphics g = image2.getGraphics();
        g.setColor(panel.getBackground());
        g.fillRect(0, 0, width, height);
        g.drawImage(image, 0, 0, panel);

        /* Write file */
        try {
            ImageIO.write(image2, extension, new java.io.File(filename));
        } catch (final java.io.IOException e) {
            System.err.println("Unable to save image:\n" + e);
        }
    }
    
    /** 
     * Will sleep for the given number of milliseconds. i.e. To
     * sleep for one second, pass 1000 as the parameter. 
     */
    public void sleep(int millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            // Just stop sleeping on interrupt
        }
    }

    /** Make drawing panel become the front-most window on the screen */
    public void toFront() {
        if (frame != null) {
            frame.toFront();
        }
    }
}
