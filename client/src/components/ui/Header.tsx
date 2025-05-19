export default function Header() {
    return (
        <>
            <div className="card rounded-none bg-indigo-400 w-full h-1/5">
                <div className="card-body flex flex-row justify-between">
                    <div>
                        <h2 className="card-title text-3xl">Quiz</h2>
                        <p>O quiz mais fácil do mundo!</p>
                    </div>
                    <div>
                        <div className="avatar avatar-placeholder">
                            <div className="w-15 bg-gray-500 rounded-full ">
                                <span className="text-3xl">N</span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

        </>

    )
}