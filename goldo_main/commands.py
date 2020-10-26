__all__  = ['trajectory']

import asyncio

import pb2 as _pb2
_sym_db = _pb2._sym_db

_futures_end_trajectory = []
_broker = None

def set_broker(broker):
    _broker = broker
    #register callbacks

def _on_propulsion_state_changed(msg):
    for future in _futures_end_trajectory:
        future.set_result(True)
    _futures_end_trajectory = []
    

def translation(distance, speed):
    msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteTranslation')(distance=distance, speed=speed)
    _broker.publishTopic('propulsion/execute_translation', msg)
    future = asyncio.Future()
    _futures_end_trajectory.append(future)
    return future

    