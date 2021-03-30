from core.signals import Signal


_payment_before_query_signal_params = ["user", "additional_filter", "filters"]
signal_before_payment_query = Signal(providing_args=_payment_before_query_signal_params)