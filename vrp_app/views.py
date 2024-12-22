import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
from .genetic_algorithm import GeneticAlgorithm

def run_genetic_algorithm(request):
    if request.method == 'POST':
        # Get form inputs
        vehicle_capacities_str = request.POST.get('vehicle_capacities', '3,3,3')
        location_points_str = request.POST.get('location_points', '(2,3),(5,6),(8,9)')

        # Parse inputs
        vehicle_capacities = list(map(int, vehicle_capacities_str.split(',')))
        location_points = [
            tuple(map(int, point.strip('()').split(',')))
            for point in location_points_str.split('),(')
        ]
        depot = (0, 0)

        # Run the Genetic Algorithm
        ga = GeneticAlgorithm(location_points, vehicle_capacities, depot=depot)
        best_route = ga.get_best_route()

        # Plot the route
        fig, ax = plt.subplots(figsize=(10, 8))
        x_coords = [point[0] for point in best_route]
        y_coords = [point[1] for point in best_route]
        ax.plot(x_coords, y_coords, marker='o', label='Optimal Route')
        ax.scatter(depot[0], depot[1], c='red', marker='D', label='Depot')
        for point in location_points:
            ax.text(point[0], point[1], f'{point}')
        ax.legend()
        ax.grid()

        # Encode the plot to Base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        plt.close(fig)
        route_image = base64.b64encode(image_png).decode('utf-8')

        # Render the template with the image
        return render(request, 'vrp_app/run_genetic_algorithm.html', {
            'route_image': route_image,
            'best_route': best_route,
        })

    return render(request, 'vrp_app/run_genetic_algorithm.html')
