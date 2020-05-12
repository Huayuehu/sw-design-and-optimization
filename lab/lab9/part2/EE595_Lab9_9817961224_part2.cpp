#include <iostream>
#include <math.h>
#include <fstream>
// #include <ifstream>
#include <random>
#include <algorithm>
#include <time.h>
#include <stdio.h>
#include <ctime>
using namespace std;

// global variables
double T0 = 80;
double beta = 0.9;
const double P = 0.8;
int num_cities;
int x_coordinate[10];
int y_coordinate[10];
int z_coordinate[10];
const double THRESHOLD = 1e-5;
const int ITERATION_ROUND = 80000;


class State {
public:
    int city_route[10];
    State() {
        for (int i = 0; i < num_cities; i++) {
            city_route[i] = i;
        }
        unsigned seed = (int)time(NULL);
        auto gen = std::default_random_engine(seed);
        shuffle(begin(city_route), end(city_route), gen);
    }
    State(int city_route[10]) {
        for (int i = 0; i < num_cities; i++) {
            this->city_route[i] = city_route[i];
        }
    }
    double calculate_distance() {
        double distance_sum = 0;
        for (int i = 0; i < num_cities; i++) {
            double delta_x, delta_y, delta_z, distance;
            if (i == num_cities - 1) {
                delta_x = x_coordinate[city_route[i]] - x_coordinate[city_route[0]];
                delta_y = y_coordinate[city_route[i]] - y_coordinate[city_route[0]];
                delta_z = z_coordinate[city_route[i]] - z_coordinate[city_route[0]];
                distance = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z);
                distance_sum += distance;
                return distance_sum;
            }
            // calculate distance between city_route[i] and city_route[i + 1]
            delta_x = x_coordinate[city_route[i]] - x_coordinate[city_route[i + 1]];
            delta_y = y_coordinate[city_route[i]] - y_coordinate[city_route[i + 1]];
            delta_z = z_coordinate[city_route[i]] - z_coordinate[city_route[i + 1]];
            distance = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z);
            distance_sum += distance;
        }
        return distance_sum;
    }
    State new_state_generator() {
        State new_state = State(this->city_route);

        int swap1 = -1, swap2 = -1;
        while (swap1 == swap2) {
            swap1 = rand() % num_cities;
            swap2 = rand() % num_cities;
        }
        int temp = new_state.city_route[swap1];
        new_state.city_route[swap1] = new_state.city_route[swap2];
        new_state.city_route[swap2] = temp;

        return new_state;
    }
};

void T0_specify_generator(State init_state, double beta_curr) {
    int count = 0;
    double T0_specify_delta = 0;
    double T = T0;
    State curr_state = init_state.new_state_generator();
    while (T > THRESHOLD && count < ITERATION_ROUND) {
        State new_state = curr_state.new_state_generator();
        double curr_distance = curr_state.calculate_distance();
        double new_distance = new_state.calculate_distance();
        double delta = (new_distance - curr_distance) / curr_distance;

        double r = rand() / double(RAND_MAX);
        if (delta < 0 || (delta >= 0 && exp(-delta / T) > r)) {
            curr_state = new_state;
            count = 0;

            if (delta > 0 && exp(-delta / T) > r) {
                T0_specify_delta += delta;
            }

            T = T * beta_curr;
        } else count++;
    }
    double T0_specify = (-T0_specify_delta) / log(P);
    // cout << "T0_Specify = " << T0_specify << endl;
}


State simulated_annealing(State init_state, double beta_curr) {
    State curr_state = State(init_state.city_route);
    State best_state = State(init_state.city_route);
    State best_state_before = State(init_state.city_route);
    double T = T0;
    int count = 0, check = 0;
    while (T > THRESHOLD) {
        State new_state = curr_state.new_state_generator();
        double curr_distance = curr_state.calculate_distance();
        double new_distance = new_state.calculate_distance();

        double r = rand() / double(RAND_MAX);
        if (curr_distance > new_distance || exp((curr_distance - new_distance) / T) > r) {
            curr_state = State(new_state.city_route);
            T = T * beta_curr;

            if (curr_state.calculate_distance() < best_state.calculate_distance()) {
                best_state = State(curr_state.city_route);
            }
        }


        count++;
        check++;
        if (check == ITERATION_ROUND) {
            if (best_state.calculate_distance() == best_state_before.calculate_distance()) {
                return best_state;
            }
            else {
                check = 0;
                best_state_before = State(best_state.city_route);
            }
        }
    }
    return best_state;
}

int main() {
    // read in input.txt
    ifstream fin("input_tsp.txt");
    if (!fin.is_open()) {
        cout << "input file fails to open." << endl;
        return 0;
    }
    fin >> num_cities;
    int name;
    for (int i = 0; i < num_cities; i++) {
        fin >> name;
        fin >> x_coordinate[i];
        fin >> y_coordinate[i];
        fin >> z_coordinate[i];
    }

    srand((int)time(NULL));
    State init_state = State();
    State best_state = simulated_annealing(init_state, beta);

    // write result to result.txt
    ofstream fout("output_tsp.txt");
    fout << "Final Distance of SA Method: " << best_state.calculate_distance() << endl;
    cout << "Final Distance of SA Method: " << best_state.calculate_distance() << endl;
    for (int i = 0; i < num_cities; i++) {
        fout << best_state.city_route[i] + 1 << endl;
        cout << best_state.city_route[i] + 1 << endl;
    }

    double beta1 = 0.92;
    T0_specify_generator(init_state, beta1);
    State best_state1 = simulated_annealing(init_state, beta1);
    cout << "beta1 -- Final Distance of SA Method: " << best_state1.calculate_distance() << endl;

    double beta2 = 0.95;
    T0_specify_generator(init_state, beta2);
    State best_state2 = simulated_annealing(init_state, beta2);
    cout << "beta2 -- Final Distance of SA Method: " << best_state2.calculate_distance() << endl;

    double beta3 = 0.97;
    T0_specify_generator(init_state, beta3);
    State best_state3 = simulated_annealing(init_state, beta3);
    cout << "beta3 -- Final Distance of SA Method: " << best_state3.calculate_distance() << endl;

    double beta4 = 0.99;
    T0_specify_generator(init_state, beta4);
    State best_state4 = simulated_annealing(init_state, beta4);
    cout << "beta3 -- Final Distance of SA Method: " << best_state4.calculate_distance() << endl;

}