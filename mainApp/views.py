import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .LengthConversion import LengthConversion
from .TemperatureConversion import TemperatureConverter
from .WeightConversion import WeightConversion
from rest_framework.views import APIView

length = LengthConversion()
temperature = TemperatureConverter()
weight = WeightConversion()

def Home(request):
    result = None
    form_data = {}
    if request.method == 'POST':
        measurement = request.POST.get('measurement')
        value_str = request.POST.get('value')
        from_ = request.POST.get('from')
        to = request.POST.get('to')
        form_data = {'measurement': measurement, 'value': value_str, 'from': from_, 'to': to}
        
        if all([measurement, value_str, from_, to]):
            try:
                value = float(value_str)
                if measurement == 'length':
                    result = length.convert(from_, value, to)
                elif measurement == 'temperature':
                    result = temperature.convert(value, from_, to)
                elif measurement == 'weight':
                    result = weight.convert(value, from_, to)
                else:
                    result = 'Invalid measurement type'
            except ValueError:
                result = 'Invalid value'
        else:
            result = 'Missing parameters'
    
    return render(request, 'home.html', {'result': result, 'form_data': form_data, 'form_data_json': json.dumps(form_data)})

def UnitConverter(request):
    # Only allow POST requests
    if request.method == 'POST':
        measurement = request.POST.get('measurement')
        value_str = request.POST.get('value')
        from_ = request.POST.get('from')
        to = request.POST.get('to')
        
        # Basic validation
        if not all([measurement, value_str, from_, to]):
            return JsonResponse({'error': 'Missing parameters'}, status=400)
            
        try:
            value = float(value_str)
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid value provided'}, status=400)

        # Route to the correct converter
        if measurement == 'length':
            result = length.convert(from_, value, to)
        elif measurement == 'weight':
            result = weight.convert(value, from_, to)
        elif measurement == 'temperature':
            result = temperature.convert(value, from_, to)
        else:
            return JsonResponse({'error': 'Invalid measurement type'}, status=400)
        
        return JsonResponse({'result': result})

    # For GET or other methods, inform the client that it's not allowed
    return HttpResponse('Method not allowed', status=405)



class UnitConverterAPI(APIView):
    def post(self,request):
            # if re/quest.method == 'POST':
            measurement = request.data.get('measurement')
            value_str = request.data.get('value')
            from_ = request.data.get('from')
            to = request.data.get('to')
            # Basic validation
            if not all([measurement, value_str, from_, to]):
                return JsonResponse({'error': 'Missing parameters'}, status=400)
                
            try:
                value = float(value_str)
            except (ValueError, TypeError):
                return JsonResponse({'error': 'Invalid value provided'}, status=400)

            # Route to the correct converter
            if measurement == 'length':
                result = length.convert(from_, value, to)
            elif measurement == 'weight':
                result = weight.convert(value, from_, to)
            elif measurement == 'temperature':
                result = temperature.convert(value, from_, to)
            else:
                return JsonResponse({'error': 'Invalid measurement type'}, status=400)
            
            return JsonResponse({'result': result})

        # For GET or other methods, inform the client that it's not allowed
            return HttpResponse('Method not allowed', status=405)
