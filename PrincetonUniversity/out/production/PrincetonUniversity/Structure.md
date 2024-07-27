public class UF {
    // Initializing union-find data structure with
    // N object (0 to N - 1)
    UF(int N)

    // Add connection between p and q
    void union(int p, int q)

    // Are p and q in the same component ?
    boolean connected(int p, int q)

    // Component identifier for p (0 to N - 1)
    int find(int p)

    // number of component
    int count()
}
