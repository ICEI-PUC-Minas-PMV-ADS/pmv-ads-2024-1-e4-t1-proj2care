import RequestCard from "../RequestCard/RequestCard"
import { useState } from "react";

const RequestList = () => {

    const [acceptedChecked, setAcceptedChecked] = useState(true);
    const [declinedChecked, setDeclinedChecked] = useState(true);
    const [pendingChecked, setPendingChecked] = useState(true);

    return (
        <div>
            <div style={{textAlign:'left'}}>
                {/* <h1>Veja suas propostas: </h1> */}
                <div className="filter">
                    <div>
                        <input type="checkbox" className="checkbox" checked={acceptedChecked} onChange={() => setAcceptedChecked(!acceptedChecked)}></input>
                        <label>Aceitas</label>
                    </div>
                    <div>
                        <input type="checkbox" className="checkbox" checked={declinedChecked} onChange={() => setDeclinedChecked(!declinedChecked)}></input>
                        <label>Recusadas</label>
                    </div>
                    <div>
                        <input type="checkbox" className="checkbox" checked={pendingChecked} onChange={() => setPendingChecked(!pendingChecked)}></input>
                        <label>Pendentes</label>
                    </div>
                </div>
                <a href='/request'><button>Envie sua proposta</button></a>
            </div>
            <div className='requestList'>
                <RequestCard></RequestCard>
                <RequestCard></RequestCard>
                <RequestCard></RequestCard>
                <RequestCard></RequestCard>
                <RequestCard></RequestCard>
                <RequestCard></RequestCard>
            </div>
        </div>
    )
}

export default RequestList